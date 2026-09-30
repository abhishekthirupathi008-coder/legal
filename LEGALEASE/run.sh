#!/usr/bin/env bash
set -e
uvicorn legalEaseAPI.main:app --reload &
BACKEND_PID=$!
trap 'kill $BACKEND_PID 2>/dev/null || true' EXIT
sleep 2
streamlit run frontend/app.py
