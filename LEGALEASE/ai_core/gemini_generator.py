import os
from typing import Optional

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


class GeminiDocumentGenerator:
    """Generate an AI-assisted first draft of a legal document."""

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        self.api_key = (api_key or os.getenv("GEMINI_API_KEY", "")).strip()
        self.model_name = (model or os.getenv("GEMINI_MODEL", "gemini-2.5-flash")).strip()
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is missing. Add it to the .env file.")
        self.client = genai.Client(api_key=self.api_key)

    @staticmethod
    def build_prompt(document_type: str, parties: str, terms: str, dates: str) -> str:
        return f"""You are LegalEase, an AI-assisted legal document drafting assistant.

Create a professional FIRST DRAFT of the requested legal document using only the information supplied by the user.

DOCUMENT TYPE:
{document_type}

PARTIES:
{parties}

TERMS / REQUIREMENTS:
{terms}

DATES:
{dates}

RULES:
1. Do not invent names, addresses, dates, amounts, laws, facts, or obligations.
2. If important information is missing, use clear placeholders such as [INSERT NAME], [INSERT DATE], or [INSERT AMOUNT].
3. Use professional legal language and clear numbered sections.
4. Include sensible sections appropriate to the document type, but do not invent material facts.
5. Keep the draft editable and easy to review.
6. Do not claim that the document is legally valid in every jurisdiction.
7. Do not provide personalized legal advice.
8. Return plain text only; do not use Markdown code fences.
9. End with this exact notice:

AI DRAFT NOTICE:
This document was generated with AI assistance and is intended as a draft for review. It is not a substitute for professional legal advice.

Return only the document content."""

    def generate_document(self, document_type: str, parties: str, terms: str, dates: str) -> str:
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=self.build_prompt(document_type, parties, terms, dates),
            config=types.GenerateContentConfig(
                temperature=0.2,
                max_output_tokens=8000,
            ),
        )
        text = getattr(response, "text", None)
        if not text:
            raise RuntimeError("Gemini returned an empty document.")
        return text.strip()
