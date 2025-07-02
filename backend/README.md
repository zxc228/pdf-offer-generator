# Backend: PDF Offer Generator

This is a FastAPI backend application for automatically generating commercial offers in PDF format based on selected services.

---

## Technologies

- **FastAPI** — modern Python web framework
- **SQLite** — embedded database
- **SQLAlchemy** — ORM
- **Pydantic** — data validation
- **Jinja2 + WeasyPrint** — PDF generation from HTML templates
- **Docker** — containerization

---

## Environment Variables (.env)
1. Copy `.env.example` → `.env`  
2. Edit the values if necessary

```bash
cp .env.example .env
```

---

## Quick Start

### 1. Using Docker

```bash
docker compose up --build
```
The service will be available at: http://localhost:8000

### 2. Regular (local) launch
>Make sure Python 3.11+ and pip are installed.

#### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

#### 2. Install dependencies
```bash
pip install -r requirements.txt
```

#### 3. Start the server
```bash
uvicorn main:app --reload
```

---

## Project Structure
```bash
server/
├── main.py                  # FastAPI entry point
├── config.py                # .env loader
├── database.py              # SQLAlchemy + initialization
├── models/                  # SQLAlchemy models
├── routes/                  # API endpoints
├── schemas/                 # Pydantic schemas
├── utils/                   # PDF generation, email (future)
├── templates/               # HTML template for PDF
├── generated/               # Generated PDF files
├── Dockerfile               # Docker instructions
├── .env                     # Configuration (DB URL, etc.)
└── requirements.txt         # Python dependencies
```

---

## API Endpoints
Available via Swagger UI: http://localhost:8000/docs

---

## Demo Version Limitations
- Email sending is not implemented, only PDF generation
- Services cannot be edited/added — a preset list is used

