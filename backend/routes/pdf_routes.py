from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List
from utils.pdf_generator import generate_pdf

router = APIRouter()

class PDFServiceItem(BaseModel):
    name: str
    description: str | None = None
    price: float

class PDFRequest(BaseModel):
    client_name: str
    company_name: str
    discount: float
    services: List[PDFServiceItem]

@router.post("/generate-pdf")
def generate_proposal_pdf(data: PDFRequest):
    total = sum(s.price for s in data.services)
    total_with_discount = total * (1 - data.discount / 100)

    pdf_path = generate_pdf({
        "client_name": data.client_name,
        "company_name": data.company_name,
        "services": data.services,
        "discount": data.discount,
        "total": round(total_with_discount, 2)
    })

    return FileResponse(pdf_path, media_type="application/pdf", filename="proposal.pdf")
