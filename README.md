# Multimodal Photo Management System

**AI-Powered Multimodal Photo Management**

> Architected and developed a complete Python-based system to automate the organization and enrichment of large photo libraries using Google's Gemini Multimodal models.

---

## 🎯 Core Technical Competencies

| Capability                           | Deliverable                                                                   |
| :----------------------------------- | :---------------------------------------------------------------------------- |
| Full-stack Applied AI Pipeline | A sanitized MVP demonstrating Gemini 1.5 Flash integration for automated visual enrichment. |

---

## 🏗️ Architecture MVP

This project contains the foundational components of the Multimodal Photo Management pipeline:

- **`src/enrichment.py`**: The core AI module leveraging the `google-generativeai` SDK to pass raw images to `gemini-1.5-flash`.
- **`requirements.txt`**: Standard dependencies (`Pillow`, `google-generativeai`).

The full closed-source personal system includes a React UI, PostgreSQL metadata database, and background celery workers. This MVP exposes the isolated AI processing layer.

## 🚀 Usage

```bash
pip install -r requirements.txt
export GEMINI_API_KEY="your-api-key"
```

```python
from src.enrichment import analyze_photo

metadata_json = analyze_photo("vacation_photo.jpg")
print(metadata_json)
```

---

## 🔮 Future Scope & Next Steps

This system currently serves as an MVP. Future iterations will expand it into a robust pipeline and platform.

### Version 2.0: Robust Backend Pipeline
- **Strict Output Enforcement:** Use Gemini's structured output schemas to guarantee valid JSON formatting.
- **Batch Processing:** Implement an asynchronous task queue (Celery/RQ) to process bulk image ingestions in the background.
- **Database Integration:** Connect to PostgreSQL using an ORM (SQLAlchemy) to store AI metadata alongside standard image EXIF data.
- **Vector Search:** Integrate a vector database (pgvector, Pinecone, or Milvus) to enable semantic "natural language" queries over the photo library.

### Version 3.0: Intelligent Platform
- **RESTful API:** Wrap the processing layer in FastAPI to handle robust endpoints (`/upload`, `/search`).
- **Frontend UI:** Develop a responsive React/Next.js interface for intuitive gallery management and real-time processing feedback.
- **Continuous Enrichment:** Implement re-indexing pipelines to easily upgrade the entire library's metadata as newer Gemini models are released.

### Version N: Enterprise Capabilities
- **Spatial/Temporal Clustering:** Use ML algorithms (like DBSCAN) to auto-group photos into events based on time and GPS proximity.
- **Event-Driven Architecture:** Migrate to a serverless model (AWS Lambda / GCP Cloud Functions) triggered directly by cloud storage uploads.
