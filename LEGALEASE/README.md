# LegalEase — AI-Powered Legal Document Generator

## Structure

LEGALEASE/
├── ai_core/
├── docs/
├── frontend/
├── Image/
├── legalEaseAPI/
├── .env.example
├── config.py
├── requirements.txt
└── run.sh

## Windows setup

1. Open this folder in VS Code.
2. Open a terminal in the project root.
3. Create a virtual environment:

   python -m venv venv

4. Activate it:

   venv\\Scripts\\activate

5. Install dependencies:

   pip install -r requirements.txt

6. Copy `.env.example` to `.env` and put your Gemini API key in it.
7. Start the backend in terminal 1:

   uvicorn legalEaseAPI.main:app --reload

8. Start the frontend in terminal 2:

   streamlit run frontend/app.py

9. Open the Streamlit URL shown by the terminal, normally http://localhost:8501.

Backend docs: http://127.0.0.1:8000/docs

## Important

This application creates AI-assisted drafts. It does not guarantee legal validity and is not a substitute for professional legal advice.
