# AI Application Generator

A compiler-style AI system that converts natural language prompts into structured software architecture, schemas, validation pipelines, and executable runtime components.

---
# Live Demo

Streamlit App:

https://ai-app-generator-ahsxvlupkbfdbffb6x3wh.streamlit.app/
---

# Features

- Intent Extraction
- System Architecture Generation
- Schema Generation
- Validation Engine
- Repair Engine
- Runtime API Generation
- Benchmark Testing
- Metrics Tracking
- Streamlit UI

---

# Architecture Pipeline

```text
User Prompt
    ↓
Intent Extraction
    ↓
Architecture Design
    ↓
Schema Generation
    ↓
Validation
    ↓
Repair Engine
    ↓
Runtime Execution
```

---

# Project Structure

```text
ai-app-generator/
│
├── app/
│   ├── generators/
│   ├── validators/
│   ├── runtime/
│   ├── schemas/
│   ├── prompts/
│   ├── main.py
│   └── runtime_runner.py
│
├── evaluation/
│   ├── metrics.py
│   ├── run_benchmark.py
│   └── test_dataset.py
│
├── frontend.py
├── test.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Tech Stack

- Python
- Streamlit
- FastAPI
- Groq API
- Pydantic

---

# Example Prompt

```text
Build a hospital management system with:
- patients
- doctors
- appointments
- billing
- admin dashboard
```

---

# Example Output

- Intent Extraction
- Architecture Design
- API Schemas
- Database Schemas
- Validation Reports

---

# Validation System

The system validates:

- schema structure
- API consistency
- database consistency
- role permissions
- missing entities

---

# Benchmarking

The project includes:

- automated benchmark runner
- edge-case prompts
- latency tracking
- success rate tracking
- repair metrics

---

# Run Locally

## Install

```bash
pip install -r requirements.txt
```

## Add Environment Variable

Create `.env`

```env
GROQ_API_KEY=your_api_key
```

## Run Streamlit App

```bash
streamlit run frontend.py
```

---

# Design Decisions

- Multi-stage pipeline for deterministic generation
- Validation treated as a first-class system component
- Repair engine regenerates only failed sections
- Modular architecture for scalability

---

# Future Improvements

- Dynamic database generation
- Auto-generated frontend code
- Async execution pipeline
- Caching layer
- Advanced repair strategies

---

# Author

Sanket Kolhe
