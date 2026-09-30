from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from ai_core.generator import LegalDocumentGenerator

router = APIRouter()
_generator: Optional[LegalDocumentGenerator] = None


class DocumentRequest(BaseModel):
    document_type: str = Field(..., min_length=2, max_length=100)
    parties: str = Field(..., min_length=2, max_length=10000)
    terms: str = Field(..., min_length=2, max_length=20000)
    dates: str = Field(default="Not specified", max_length=2000)


class DocumentResponse(BaseModel):
    success: bool
    document_type: str
    content: str


def get_generator() -> LegalDocumentGenerator:
    global _generator
    if _generator is None:
        _generator = LegalDocumentGenerator()
    return _generator


@router.get("/")
def home():
    return {"message": "LegalEase API is running", "version": "1.0.0"}


@router.get("/health")
def health():
    return {"status": "healthy"}


@router.post("/generate", response_model=DocumentResponse)
def generate_document(request: DocumentRequest):
    try:
        content = get_generator().generate(
            document_type=request.document_type,
            parties=request.parties,
            terms=request.terms,
            dates=request.dates,
        )
        return DocumentResponse(
            success=True,
            document_type=request.document_type,
            content=content,
        )
    except ValueError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Document generation failed: {exc}") from exc
