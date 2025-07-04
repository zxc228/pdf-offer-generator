# Code Forge | PDF Offer Generator

A full-stack solution for generating commercial offers in PDF format with a branded “forge” style.  
Includes a modern Next.js frontend and a FastAPI backend. The manager fills out a form, selects services, and downloads a ready-made PDF offer.

---

## Features

- Stylish dark-themed interface with “Code Forge” branding
- Easy form for entering client info and selecting services
- Automatic PDF generation and download (via backend)
- Service list is loaded from the backend API
- Email sending (planned/production only)
- Docker support for easy deployment

---

## Technologies

**Frontend:**
- [Next.js 14](https://nextjs.org/) (React)
- [Tailwind CSS](https://tailwindcss.com/) for styling
- TypeScript (TSX)

**Backend:**
- [FastAPI](https://fastapi.tiangolo.com/) — Python web framework
- SQLite — embedded database
- SQLAlchemy — ORM
- Pydantic — data validation
- Jinja2 + WeasyPrint — PDF generation from HTML templates

**Other:**
- Docker & Docker Compose

---

## Quick Start

### 1. Using Docker (recommended)

> Runs both frontend and backend together.
1. Go to `/backend`  
2. Copy environment variables and install dependencies:

    ```bash
    cd backend
    cp .env.example .env
    cd ..
```

```bash
docker compose up --build
```

- Frontend: [http://localhost:3000](http://localhost:3000)
- Backend: [http://localhost:8000](http://localhost:8000)
- API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 2. Manual Launch (development)

#### Backend

1. Go to `/backend`  
2. Copy environment variables and install dependencies:

    ```bash
    cp .env.example .env
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Start the backend server:

    ```bash
    uvicorn main:app --reload
    ```

#### Frontend

1. Go to `/frontend`  
2. Install dependencies:

    ```bash
    npm install
    ```

3. Start the dev server:

    ```bash
    npm run dev
    ```

4. Open [http://localhost:3000](http://localhost:3000)

**Note:** The backend must be running for the frontend to work.

---

## Environment Variables

### Backend (`/backend/.env`)
- See `.env.example` for required variables (e.g., database URL)

### Frontend (`/frontend/.env.local`)
- `NEXT_PUBLIC_API_URL` — backend address (default: `http://backend:8000` in Docker, `http://localhost:8000` for local dev)

---

## Project Structure

```bash
backend/
  main.py         # FastAPI entry point
  config.py       # .env loader
  database.py     # SQLAlchemy + initialization
  models/         # SQLAlchemy models
  routes/         # API endpoints
  schemas/        # Pydantic schemas
  utils/          # PDF generation, email (future)
  templates/      # HTML template for PDF
  generated/      # Generated PDF files
  Dockerfile      # Backend Docker instructions
  .env            # Backend config
  requirements.txt

frontend/
  src/
    app/          # Next.js app router (pages)
    components/   # UI components
    lib/          # API clients
  public/         # Static files and logos
  Dockerfile      # Frontend Docker instructions
  .env.local      # Frontend config
  package.json
  tailwind.config.js

docker-compose.yaml  # Orchestration for frontend + backend
```

---

## API Endpoints

- Available via Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Demo Version Limitations

- Email sending is not implemented, only PDF generation
- Services cannot be edited or added — a preset list is used

---