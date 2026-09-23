"""
Synthetic dashboard warning-light dataset generator.

This project's Extended Track needs an image dataset for the CV/YOLO
component. Since a licensed real-world photo dataset of dashboard warning
lights was not available for this environment, this script procedurally
generates a small labeled dataset of simple dashboard icon renderings
(check engine, battery, oil pressure, brake, coolant temperature) with
YOLO-format bounding box labels.

For a real submission, swap this synthetic set for actual photos/scraped
images of dashboards (with correct licensing) — the notebook and backend
code do not care where the images came from, only that
data/images/{train,val}/ and data/images/labels/{train,val}/ follow the
same YOLO layout produced here.
"""
import os
import random
from PIL import Image, ImageDraw

random.seed(42)

CLASSES = ["check_engine", "battery", "oil_pressure", "brake", "coolant_temp"]
OUT_DIR = os.path.join(os.path.dirname(__file__), "images")
IMG_SIZE = 320
N_TRAIN = 80
N_VAL = 20


def draw_icon(draw, cls, cx, cy, s, color):
    """Draw a simple vector-style icon for a dashboard warning light."""
    if cls == "check_engine":
        # simple engine block silhouette
        draw.rectangle([cx - s, cy - s * 0.6, cx + s, cy + s * 0.6], outline=color, width=3)
        draw.rectangle([cx - s * 0.5, cy - s, cx + s * 0.5, cy - s * 0.6], outline=color, width=3)
    elif cls == "battery":
        draw.rectangle([cx - s, cy - s * 0.7, cx + s, cy + s * 0.7], outline=color, width=3)
        draw.line([cx - s * 0.3, cy - s * 0.9, cx - s * 0.3, cy - s * 0.7], fill=color, width=3)
        draw.line([cx + s * 0.3, cy - s * 0.9, cx + s * 0.3, cy - s * 0.7], fill=color, width=3)
        draw.text((cx - s * 0.25, cy - s * 0.35), "+ -", fill=color)
    elif cls == "oil_pressure":
        # oil can silhouette (triangle + spout)
        draw.polygon([(cx - s, cy + s), (cx + s, cy + s), (cx, cy - s)], outline=color, width=3)
        draw.line([(cx + s * 0.6, cy - s * 0.6), (cx + s * 1.3, cy - s * 1.1)], fill=color, width=3)
    elif cls == "brake":
        draw.ellipse([cx - s, cy - s, cx + s, cy + s], outline=color, width=3)
        draw.text((cx - s * 0.35, cy - s * 0.4), "!", fill=color)
    elif cls == "coolant_temp":
        draw.rectangle([cx - s * 0.25, cy - s, cx + s * 0.25, cy + s * 0.6], outline=color, width=3)
        draw.ellipse([cx - s * 0.45, cy + s * 0.5, cx + s * 0.45, cy + s * 1.3], outline=color, width=3)
        # wavy "heat" line to the side
        draw.line([cx + s * 0.7, cy - s * 0.5, cx + s, cy - s * 0.9], fill=color, width=2)


def gen_image(idx, split):
    img = Image.new("RGB", (IMG_SIZE, IMG_SIZE), color=(18, 18, 22))
    draw = ImageDraw.Draw(img)

    n_icons = random.choice([1, 1, 1, 2])
    used = random.sample(CLASSES, k=n_icons)
    labels = []

    for cls in used:
        s = random.randint(28, 48)
        cx = random.randint(s + 10, IMG_SIZE - s - 10)
        cy = random.randint(s + 10, IMG_SIZE - s - 10)
        color = random.choice([(255, 60, 60), (255, 180, 40), (255, 220, 60), (255, 255, 255)])
        draw_icon(draw, cls, cx, cy, s, color)

        # bounding box in pixels -> YOLO normalized (x_center, y_center, w, h)
        pad = s * 1.4
        x0, y0 = max(0, cx - pad), max(0, cy - pad)
        x1, y1 = min(IMG_SIZE, cx + pad), min(IMG_SIZE, cy + pad)
        bw, bh = x1 - x0, y1 - y0
        xc, yc = (x0 + x1) / 2, (y0 + y1) / 2
        cls_id = CLASSES.index(cls)
        labels.append(f"{cls_id} {xc/IMG_SIZE:.6f} {yc/IMG_SIZE:.6f} {bw/IMG_SIZE:.6f} {bh/IMG_SIZE:.6f}")

    # light dashboard-panel texture: a few faint gauge arcs
    for _ in range(2):
        gx, gy = random.randint(0, IMG_SIZE), random.randint(0, IMG_SIZE)
        draw.arc([gx - 60, gy - 60, gx + 60, gy + 60], 200, 340, fill=(40, 40, 46), width=2)

    img_dir = os.path.join(OUT_DIR, split, "images")
    lbl_dir = os.path.join(OUT_DIR, split, "labels")
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(lbl_dir, exist_ok=True)
    fname = f"dash_{split}_{idx:04d}"
    img.save(os.path.join(img_dir, fname + ".jpg"), quality=90)
    with open(os.path.join(lbl_dir, fname + ".txt"), "w") as f:
        f.write("\n".join(labels))


def main():
    for i in range(N_TRAIN):
        gen_image(i, "train")
    for i in range(N_VAL):
        gen_image(i, "val")

    with open(os.path.join(OUT_DIR, "classes.txt"), "w") as f:
        f.write("\n".join(CLASSES))

    # data.yaml for ultralytics YOLO training/inference
    yaml_content = f"""path: {OUT_DIR}
train: train/images
val: val/images
names:
"""
    for i, c in enumerate(CLASSES):
        yaml_content += f"  {i}: {c}\n"
    with open(os.path.join(OUT_DIR, "data.yaml"), "w") as f:
        f.write(yaml_content)

    print(f"Generated {N_TRAIN} train and {N_VAL} val images with YOLO labels.")
    print(f"Classes: {CLASSES}")


if __name__ == "__main__":
    main()
