# Multimodal Photo Management System

**AI-Powered Multimodal Photo Management**

> Architected and developed a complete Python-based system to automate the organization and enrichment of large photo libraries using Google's Gemini Multimodal models.

---

## 🎯 Resume Claim Covered

| Claim ID   | Capability                           | Deliverable                                                                   |
| :--------- | :----------------------------------- | :---------------------------------------------------------------------------- |
| **AI_PROJ_01** | Full-stack Applied AI Pipeline | A sanitized MVP demonstrating Gemini 1.5 Flash integration for automated visual enrichment. |

---

## 🏗️ Architecture MVP

This repository contains the foundational components of the Multimodal Photo Management pipeline:

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
