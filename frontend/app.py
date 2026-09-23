import os
import gradio as gr
from dotenv import load_dotenv
from api_client import ask, check_health, ApiError, API_BASE_URL

load_dotenv()

def get_system_status():
    try:
        health = check_health()
        return (
            "Connected",
            f"{health.get('chunk_count', 0)} Chunks ({health.get('embedding_mode', 'N/A')})",
            "Active" if health.get("yolo_loaded") else "Unavailable",
            API_BASE_URL,
        )
    except Exception as e:
        return ("Offline", "Unavailable", "Unavailable", str(e))

import re

def process_query(message, history, image):
    if history is None:
        history = []

    if not message and image is None:
        return "", history, "Please enter a diagnostic query or provide an instrument cluster image.", ""

    image_bytes = None
    if image is not None:
        with open(image, "rb") as f:
            image_bytes = f.read()

    query_text = message if message else "Diagnose active indicators on this instrument panel."

    try:
        result = ask(query_text, image_bytes=image_bytes)
        
        raw_answer = result.get("answer", "No diagnostics available.").strip()
        raw_sources = result.get("sources", [])
        sources_str = ", ".join(raw_sources) or "None identified"
        mode = result.get("generation_mode", "N/A")
        
        cleaned_answer = re.sub(r'\(?\s*source[s]?\s*:\s*[^)]+\)?', '', raw_answer, flags=re.IGNORECASE)
        cleaned_answer = re.sub(r'According to the provided (sources?|context)[,\s]*', '', cleaned_answer, flags=re.IGNORECASE)
        cleaned_answer = cleaned_answer.strip()
        if cleaned_answer:
            cleaned_answer = cleaned_answer[0].upper() + cleaned_answer[1:]
        else:
            cleaned_answer = raw_answer

        detections = result.get("detections", [])
        if detections:
            detected_str = " • ".join([f"{d['label']} [{d['confidence']:.0%}]" for d in detections])
        else:
            detected_str = "No active warning indicators flagged."

        citation_footer = "\n\n" + "—" * 30 + "\n"
        if raw_sources:
            unique_sources = sorted(list(set(raw_sources)))
            formatted_sources = ", ".join([f"`{src}`" for src in unique_sources])
            citation_footer += f"**Sources:** {formatted_sources}"
        else:
            citation_footer += "**Sources:** `None identified`"

        if detections:
            citation_footer += f"\n**Detections:** {detected_str}"

        full_assistant_reply = f"{cleaned_answer}{citation_footer}"

        meta_info = f"**Pipeline Mode:** `{mode}`\n\n**Grounding Sources:** `{sources_str}`"
        detection_info = f"**Vision Detections:** {detected_str}"

        user_label = message if message else "[Dashboard Scan Uploaded]"
        
        history.append({"role": "user", "content": user_label})
        history.append({"role": "assistant", "content": full_assistant_reply})

        return "", history, meta_info, detection_info

    except ApiError as e:
        user_label = message if message else "[Dashboard Scan Uploaded]"
        history.append({"role": "user", "content": user_label})
        history.append({"role": "assistant", "content": f"Service Notice: {str(e)}"})
        return "", history, "Backend communication failure", "N/A"

custom_css = """
body, .gradio-container {
    background-color: #f8fafc !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
.header-container {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    padding: 22px 28px;
    border-radius: 10px;
    color: #ffffff;
    margin-bottom: 18px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}
.header-title {
    font-size: 1.65rem;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 4px;
}
.header-subtitle {
    font-size: 0.92rem;
    color: #94a3b8;
}
"""

theme = gr.themes.Base(
    primary_hue="amber",
    secondary_hue="slate",
    neutral_hue="slate",
    font=[gr.themes.GoogleFont("Inter"), "ui-sans-serif", "system-ui", "sans-serif"],
).set(
    body_background_fill="#f8fafc",
    block_background_fill="#ffffff",
    block_border_width="1px",
    block_border_color="#e2e8f0",
    button_primary_background_fill="#d97706",
    button_primary_background_fill_hover="#b45309",
    button_primary_text_color="#ffffff",
)

with gr.Blocks(title="AutoDiagnostic Pro | RAG & Vision Assistant") as demo:
    gr.HTML("""
    <div class="header-container">
        <div class="header-title">Automotive Technical Diagnostics Assistant</div>
        <div class="header-subtitle">Knowledge Retrieval System & Cluster Vision Telemetry</div>
    </div>
    """)

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("#### System Telemetry")
            with gr.Group():
                status_conn = gr.Textbox(label="API Gateway", interactive=False)
                status_chunks = gr.Textbox(label="Vector Index", interactive=False)
                status_yolo = gr.Textbox(label="Vision Model", interactive=False)
                status_url = gr.Textbox(label="Target Host", interactive=False)
                refresh_btn = gr.Button("Refresh Status", size="sm")

            gr.Markdown("#### Instrument Cluster Capture")
            input_image = gr.Image(
                label="Upload Gauge / Warning Indicator", 
                type="filepath", 
                sources=["upload", "clipboard"]
            )
            detection_output = gr.Markdown("**Vision Detections:** Ready for inspection.")

        with gr.Column(scale=2):
            chatbot = gr.Chatbot(
                label="Diagnostic Service Transcript", 
                height=480
            )
            
            with gr.Row():
                txt_input = gr.Textbox(
                    label="Technical Inquiry",
                    placeholder="Enter OBD-II trouble code, diagnostic symptom, or component specs...",
                    lines=1,
                    scale=4,
                )
                submit_btn = gr.Button("Query System", variant="primary", scale=1)

            with gr.Accordion("Knowledge Base Citations & Telemetry", open=False):
                meta_output = gr.Markdown("Citation records will be displayed following retrieval.")

            gr.Examples(
                examples=[
                    ["What does OBD-II code P0300 mean and what usually causes it?"],
                    ["My brake pedal feels soft and spongy, what should I check?"],
                    ["What is the minimum brake pad thickness before replacement?"],
                    ["What should I do if my oil pressure warning light comes on?"]
                ],
                inputs=txt_input
            )

    refresh_btn.click(
        fn=get_system_status, 
        inputs=[], 
        outputs=[status_conn, status_chunks, status_yolo, status_url]
    )
    
    demo.load(
        fn=get_system_status, 
        inputs=[], 
        outputs=[status_conn, status_chunks, status_yolo, status_url]
    )

    submit_btn.click(
        fn=process_query,
        inputs=[txt_input, chatbot, input_image],
        outputs=[txt_input, chatbot, meta_output, detection_output]
    )
    
    txt_input.submit(
        fn=process_query,
        inputs=[txt_input, chatbot, input_image],
        outputs=[txt_input, chatbot, meta_output, detection_output]
    )

if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1", 
        server_port=7860, 
        share=False,
        theme=theme,
        css=custom_css
    )