# 🔧 AutoDiagnostic Pro: Multimodal Automotive Diagnostics & Cluster Vision Assistant

**Level 2 Summer Training — Graduation Project**
**Track:** Extended (Text RAG + Computer Vision YOLOv8)
**Domain:** Automotive Diagnostics, Technical Service Manuals & Parts Catalog

AutoDiagnostic Pro is an end-to-end multimodal automotive diagnostics assistant combining Retrieval-Augmented Generation (RAG) with Computer Vision to deliver grounded, citation-based answers from technical automotive manuals and part catalogs.

Users can query the system regarding:

* OBD-II diagnostic trouble codes and fault isolation
* Engine and brake mechanical troubleshooting
* Electrical system tolerances and battery drain parameters
* OEM component part numbers and fitment rules
* Scheduled maintenance intervals and fluid service cycles
* Instrument cluster telltale warning indicators

In the **Extended Track**, users can also upload an image of a vehicle instrument panel. A fine-tuned **YOLOv8** model identifies active warning indicators and incorporates them directly into the retrieval context.

---

## 1. Overview

| Component            | Specification                                                         |
| -------------------- | --------------------------------------------------------------------- |
| **Domain**           | Automotive Diagnostics & Technical Maintenance Assistant              |
| **Track**            | Extended — Text RAG + Computer Vision YOLOv8                          |
| **Backend**          | FastAPI — RESTful API, lifespan initialization, CORS middleware       |
| **Frontend**         | Gradio 5/6 — Diagnostic telemetry console, chat history, image upload |
| **Vector Store**     | ChromaDB — Persistent vector embeddings on disk                       |
| **Embeddings**       | `sentence-transformers/all-MiniLM-L6-v2`                              |
| **LLM Engine**       | Local Ollama — `llama3.2:1b`                                          |
| **Vision Model**     | Fine-tuned YOLOv8n instrument-cluster detector                        |
| **Detected Classes** | 14 dashboard warning-indicator classes                                |
| **Testing**          | Pytest + HTTPX (`TestClient`)                                         |

---

## 2. Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                    Gradio Frontend Console                  │ (Port 7860)
│             Chat History + Cluster Image Upload             │
└──────────────────────────────┬──────────────────────────────┘
                               │ HTTP POST (JSON + Base64 Image)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                    FastAPI Backend Engine                   │ (Port 8000)
│                                                             │
│  ┌───────────────────────┐       ┌────────────────────────┐ │
│  │    Vision Service     │       │   Retrieval Service    │ │
│  │     YOLOv8n           │       │      ChromaDB          │ │
│  │      Inference        │       │     Vector Store       │ │
│  └──────────┬────────────┘       └───────────┬────────────┘ │
│             │ Detected Symbols               │ Top-K Chunks │
│             └───────────────┬────────────────┘              │
│                             ▼                               │
│  ┌───────────────────────────────────────────────────────┐  │
│  │       Generation Service                              │  │
│  │       Context Fusion + Prompt Builder                 │  │
│  └──────────────────────────┬────────────────────────────┘  │
└─────────────────────────────┼───────────────────────────────┘
                              │ Prompt + Retrieved Context
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Local Ollama Server                      │ (Port 11434)
│                        llama3.2:1b                          │
└─────────────────────────────────────────────────────────────┘
```

### Request Flow — `/query`

1. **Multimodal Fusion:** If an instrument cluster image is provided, YOLOv8 identifies active indicators and prepends the detection context to the query.
2. **Semantic Search:** Query embeddings (`all-MiniLM-L6-v2`) search ChromaDB to retrieve top-k technical manual segments.
3. **Prompt Formulation:** The retrieved context and question are fused into a constrained prompt requiring explicit source citation.
4. **Grounded Generation:** The local Ollama server running `llama3.2:1b` outputs an answer grounded in the documentation.
5. **Fallback Synthesis:** If Ollama is unreachable, an extractive fallback compiles diagnostic answers directly from the top chunk.
6. **Structured Response:** Returns answer, citations, detected symbols, and generation mode.

## 3. Tech Stack

* **RAG & NLP:** ChromaDB, Sentence Transformers (`all-MiniLM-L6-v2`), scikit-learn, PyPDF, Pandas, NumPy
* **Vision Pipeline:** Ultralytics YOLOv8n, OpenCV, Pillow
* **LLM Engine:** Ollama (`llama3.2:1b`)
* **Backend API:** FastAPI, Uvicorn, Pydantic v2, `pydantic-settings`
* **Frontend App:** Gradio 5/6, HTTPX, `python-dotenv`
* **Automated Testing:** Pytest, HTTPX `TestClient`

## 4. Project Structure

```text
automotive-diagnostics-rag-assistant/
│
├── backend/
│   ├── app/
│   │   ├── api/routes/query.py       # POST /query & GET /health endpoints
│   │   ├── core/config.py            # Environment-based configuration
│   │   ├── schemas/query.py          # Request and response models
│   │   ├── services/
│   │   │   ├── generation.py         # Prompt building & Ollama integration
│   │   │   ├── retrieval.py          # Vector store search & chunk loading
│   │   │   └── vision.py             # YOLOv8 inference & label mapping
│   │   ├── utils/logging_config.py   # Application logging
│   │   └── main.py                   # FastAPI lifespan & CORS setup
│   ├── data/vector_store/            # Persisted ChromaDB collection
│   ├── tests/test_query.py           # Pytest test suite
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── app.py                        # Gradio multimodal UI
│   ├── api_client.py                 # Backend API client
│   ├── requirements.txt
│   └── .env.example
│
├── notebooks/
│   └── rag_pipeline.ipynb            # End-to-end RAG development notebook
│
├── data/
│   ├── documents/                    # Technical manual Markdown files
│   └── models/dash_yolo_best.pt      # Fine-tuned YOLOv8 weights (<50MB)
│
├── .gitignore
└── README.md
```

## 5. Domain Knowledge Base & Vision Dataset

### 5.1 Domain Knowledge Base

| **Document**                       | **Scope & Contents**                                                                               |
| ---------------------------------- | -------------------------------------------------------------------------------------------------- |
| `obd2_trouble_codes.md`            | Powertrain, network, chassis, and body OBD-II fault codes and diagnostic protocols                 |
| `brake_system_diagnostics.md`      | Hydraulic diagnostics, rotor runout thresholds, pad friction parameters, and caliper servicing     |
| `engine_diagnostics.md`            | Compression troubleshooting, sensor misfire evaluation, oil-pressure thresholds, and cooling cycle |
| `electrical_system_diagnostics.md` | Alternator charging limits, parasitic battery drain, relay faults, and electrical diagnostics      |
| `maintenance_schedule.md`          | Recommended inspections, fluid-change intervals, and preventative safety criteria                  |
| `parts_catalog.md`                 | Component fitment information, OEM part numbers, and replacement specifications                    |

### 5.2 Extended Track — Vision Dataset

| **Property** | **Specification**                                                   |
| ------------ | ------------------------------------------------------------------- |
| **Task**     | Multi-label localization and classification of dashboard indicators |
| **Model**    | YOLOv8n fine-tuned on vehicle instrument clusters                   |
| **Output**   | Detected warning indicators, bounding boxes, and confidence scores  |

**Supported Indicator Classes:**

`Central Warning lamp`, `Doors`, `Electronic Power Steering`, `Engine cooling system`, `Low fuel level`, `Seat Belt`, `Washer Fluid`, `security`, `FrontFogLight`, `Low beam`, `SideLamp`, `LaneCenteringOff`, `Check Engine`, `Oil Pressure`.

## 6. Environment Configuration

### Backend (`backend/.env.example`)

```env
VECTOR_STORE_DIR=./data/vector_store
COLLECTION_NAME=automotive_docs
TOP_K=4

OLLAMA_HOST=http://localhost:11434
LLM_MODEL_NAME=llama3.2:1b

YOLO_WEIGHTS_PATH=../data/models/dash_yolo_best.pt
YOLO_CONFIDENCE_THRESHOLD=0.5

FRONTEND_ORIGIN=http://127.0.0.1:7860
```

### Frontend (`frontend/.env.example`)

```env
API_BASE_URL=http://localhost:8000
```

## 7. Installation & Quick Start

### Prerequisites

* Python 3.10+
* Git
* Ollama

```bash
# 1. Clone repository
git clone https://github.com/<YOUR_GITHUB_USERNAME>/automotive-diagnostics-rag-assistant.git
cd automotive-diagnostics-rag-assistant

# 2. Virtual environment setup
python -m venv .venv

# Windows:
.venv\Scripts\activate

# Linux/macOS:
source .venv/bin/activate

# 3. Dependencies installation
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt

# 4. Pull local LLM
ollama run llama3.2:1b
```

## 8. Running the Application (3 Terminals)

```powershell
# Terminal 1 — Ollama LLM Service
ollama serve

# Terminal 2 — FastAPI Backend
uvicorn backend.app.main:app --reload --port 8000

# Terminal 3 — Gradio Console
python frontend/app.py
```

* **Gradio Web Interface:** `http://127.0.0.1:7860`
* **FastAPI Documentation:** `http://127.0.0.1:8000/docs`
* **Backend Health Check:** `http://127.0.0.1:8000/health`

## 9. Verification & Automated Testing

Execute the test suite using Pytest:

```powershell
python -m pytest backend/tests/test_query.py -v
```

| **Test Function**                      | **Verification Purpose**                                                    |
| -------------------------------------- | --------------------------------------------------------------------------- |
| `test_health_check`                    | Validates database indexing readiness, collection loading, and chunk counts |
| `test_query_happy_path`                | Validates full multimodal retrieval, generation output, and cited sources   |
| `test_query_invalid_input_returns_422` | Verifies rejection of empty questions (`min_length=1`)                      |
| `test_query_missing_field_returns_422` | Ensures schema rejection on invalid or missing JSON parameters              |

## 10. API Specification

### `GET /health`

```bash
curl -X GET http://127.0.0.1:8000/health
```

```json
{
  "status": "ok",
  "vector_store_loaded": true,
  "chunk_count": 64,
  "embedding_mode": "sentence_transformers",
  "yolo_loaded": true
}
```

### `POST /query`

```bash
curl -X POST http://127.0.0.1:8000/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What does OBD-II code P0300 mean?",
    "image_base64": null
  }'
```

```json
{
  "answer": "OBD-II code P0300 indicates a Random/Multiple Cylinder Misfire Detected, meaning the ECM has detected misfires occurring irregularly across multiple cylinders.",
  "sources": [
    "obd2_trouble_codes.md"
  ],
  "generation_mode": "ollama",
  "detections": []
}
```

## 11. Evaluation & Grounding Report (Phase 2.6)

| **Test Question**                                                      | **Primary Retrieved Source**       | **Grounding Assessment**                     | **Result** |
| ---------------------------------------------------------------------- | ---------------------------------- | -------------------------------------------- | ---------- |
| What does OBD-II code P0300 mean and what causes it?                   | `obd2_trouble_codes.md`            | Grounded directly in manual definitions      | Passed     |
| My brake pedal feels soft and spongy, what should I check?             | `brake_system_diagnostics.md`      | Grounded in hydraulic-line air diagnostics   | Passed     |
| What is a normal charging voltage range for an alternator?             | `electrical_system_diagnostics.md` | Grounded in voltage-regulator specifications | Passed     |
| What should I do if my oil-pressure warning light comes on?            | `engine_diagnostics.md`            | Grounded in emergency shutdown protocol      | Passed     |
| What part number is the front ceramic brake pad set for compact sedan? | `parts_catalog.md`                 | Grounded in OEM reference cross-index        | Passed     |
| What causes a grinding noise when braking?                             | `brake_system_diagnostics.md`      | Grounded in rotor/friction-material limits   | Passed     |
| When should brake fluid be flushed?                                    | `maintenance_schedule.md`          | Grounded in preventive-service tables        | Passed     |
| What could cause the engine to crank but not start?                    | `engine_diagnostics.md`            | Grounded in ignition/fuel-supply tests       | Passed     |
| What does code P0420 mean?                                             | `obd2_trouble_codes.md`            | Grounded in catalytic-threshold tables       | Passed     |
| What is the minimum brake-pad thickness before replacement?            | `brake_system_diagnostics.md`      | Grounded in wear-indicator limits            | Passed     |

## 12. Deliverables Checklist Alignment

* [x] **`notebooks/rag_pipeline.ipynb`**: Fully executed pipeline with chunking, embeddings, retrieval verification, and evaluation tables.
* [x] **Backend**: FastAPI app with `/health` and `/query`, pinned dependencies, lifespan initialization, and Pytest coverage.
* [x] **Frontend**: Interactive Gradio chat interface with source citation cards, telemetry status, and image inspection.
* [x] **Persisted Vector Store**: ChromaDB index persisted to disk and loaded without rebuild overhead.
* [x] **Repository Governance**: Clean git tree; `.gitignore` actively excludes `.venv`, `.env`, and database caches.
* [x] **Extended Track**: Fine-tuned YOLOv8 vision pipeline fused into the RAG context.