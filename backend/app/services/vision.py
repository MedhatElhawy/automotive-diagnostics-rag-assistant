import base64
import io
import logging
from typing import List, Tuple

from app.core.config import settings

logger = logging.getLogger(__name__)

DASH_CLASS_TO_PHRASE = {
    "Central Warning lamp": "central master warning indicator lamp is on",
    "Doors": "car door ajar open warning indicator is on",
    "Electronic Power Steering": "electronic power steering EPS malfunction warning",
    "Electronic Power Steering Warning": "electronic power steering EPS system warning light",
    "Engine cooling system": "engine cooling system issue warning light",
    "FrontFogLight": "front fog lights are active",
    "High Engine Coolant Temperature": "high engine coolant temperature overheating warning",
    "LaneCenteringOff": "lane centering assist system is turned off",
    "Low beam": "low beam headlights are active",
    "Low fuel level": "low fuel level reserve indicator is on",
    "Seat Belt": "unfastened seat belt reminder indicator is on",
    "SideLamp": "side parking lamps are active",
    "Washer Fluid": "windshield washer fluid level is low",
    "security": "anti-theft vehicle security system indicator is active",
}


class VisionService:
    """Loads the fine-tuned YOLOv8 dashboard warning-light detector once at
    startup and runs inference on uploaded images (Extended Track)."""

    def __init__(self) -> None:
        self.model = None

    def load(self) -> None:
        try:
            from ultralytics import YOLO

            self.model = YOLO(settings.yolo_weights_path)
            logger.info("YOLO model loaded from %s", settings.yolo_weights_path)
        except Exception as e:
            logger.warning("YOLO model could not be loaded (%s: %s); vision features disabled.", type(e).__name__, e)
            self.model = None

    @property
    def is_loaded(self) -> bool:
        return self.model is not None

    def detect(self, image_base64: str) -> List[Tuple[str, float]]:
        if not self.is_loaded:
            raise RuntimeError("VisionService.load() must be called before detect().")

        from PIL import Image

        raw = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(raw)).convert("RGB")

        result = self.model.predict(image, verbose=False)[0]
        detections = []
        for box in result.boxes:
            label = self.model.names[int(box.cls[0])]
            confidence = float(box.conf[0])
            detections.append((label, confidence))
        return detections

    @staticmethod
    def detections_to_query_prefix(detections: List[Tuple[str, float]], conf_threshold: float = None) -> str:
        conf_threshold = conf_threshold if conf_threshold is not None else settings.yolo_confidence_threshold
        phrases = [
            DASH_CLASS_TO_PHRASE[label]
            for label, conf in detections
            if conf >= conf_threshold and label in DASH_CLASS_TO_PHRASE
        ]
        return (". ".join(phrases) + ". ") if phrases else ""


# module-level singleton, created once and reused across requests
vision_service = VisionService()
