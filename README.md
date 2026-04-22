# SafeGen API – Guardrailed GenAI Service

## Overview
SafeGen API is a lightweight backend service designed to simulate how enterprises safely integrate generative AI into applications.

Rather than exposing LLMs directly, this service acts as a controlled wrapper that enforces governance, safety, and observability.

## Key Features
- Prompt validation (guardrails)
- Output filtering
- Structured logging for auditability
- API-based architecture (FastAPI)

## Why This Matters
In enterprise environments, generative AI must be:
- Secure
- Compliant
- Observable
- Scalable

This project demonstrates how organizations can build reusable patterns to enable AI safely across teams.

## Architecture
User → API → Guardrails → (LLM simulation) → Output filter → Logging

## Run Locally
pip install -r requirements.txt  
uvicorn main:app --reload
