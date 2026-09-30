from ai_core.gemini_generator import GeminiDocumentGenerator


class LegalDocumentGenerator:
    """Application-level wrapper around the Gemini generator."""

    def __init__(self):
        self._generator = GeminiDocumentGenerator()

    def generate(self, document_type: str, parties: str, terms: str, dates: str) -> str:
        return self._generator.generate_document(document_type, parties, terms, dates)
