# Copilot Instructions

## Project overview
This repository is for a local-first Python application that combines:
- Skill training and learning notes.
- Career roadmap tracking.
- Project tracking and resume bullet generation.
- Personal finance tracking using Plaid.
- Todo and goals management.
- Unified dashboards.

## Primary tech stack
- Python
- FastAPI
- Streamlit
- SQLAlchemy
- Alembic
- SQLite for local development first
- PostgreSQL compatibility later if needed

## Architecture expectations
- Keep the code modular and easy to navigate.
- Separate API routes, schemas, models, services, and database utilities.
- Keep business logic out of route handlers.
- Prefer explicit, readable code over clever abstractions.
- Build for single-user local-first usage first.

## Product modules
- Skills and learning insights
- Career roadmap
- Projects and impact tracking
- Resume bullet generation
- Finance accounts and transactions
- Goals and todos
- Dashboards and summaries

## Backend guidance
- Use FastAPI for APIs.
- Keep routers thin.
- Put validation in Pydantic schemas.
- Put business logic in service modules.
- Use SQLAlchemy models consistently.
- Use Alembic for schema changes.

## Frontend guidance
- Use Streamlit for internal UI screens and dashboards.
- Keep pages simple, task-focused, and readable.
- Prefer reusable helpers for repeated UI patterns.
- Keep business logic outside Streamlit pages where possible.

## Data guidance
- Add created_at and updated_at fields on important entities.
- Use soft delete where history matters.
- Keep naming predictable and consistent.
- Normalize finance data enough to support analytics later.

## Finance module rules
- Start Plaid work in sandbox mode.
- Never hardcode secrets or tokens.
- Keep ingestion logic separate from dashboard logic.
- Design transaction sync so incremental updates can be supported.

## Resume module rules
- Generate resume bullets from structured project evidence.
- Store source project facts separately from generated resume text.
- Keep statuses like draft, approved, and archived.

## Coding preferences
- Use descriptive names.
- Prefer small focused functions.
- Add comments only when they improve clarity.
- Avoid unnecessary dependencies.
- Make minimal, targeted changes.
- always explain assumptions and reasoning in comments when implementing new features or making non-obvious changes.
- developer building the application is not an expert in all domains, so clear explanations are crucial for maintainability and future contributions.
- keep your responses concise and small and focused. Dont try to solve everything at once. It's better to make incremental improvements and get feedback than to implement a large change that may not fit the project's needs or style.


## Copilot behavior
- Follow the existing folder structure.
- Suggest changes that fit the current architecture.
- When adding a feature, consider whether model, schema, service, API, and UI all need updates.
- Prefer maintainable solutions over overly clever ones.
- If requirements are ambiguous, implement the simplest extensible version first.

## Do not
- Do not replace FastAPI or Streamlit unless explicitly asked.
- Do not move to microservices.
- Do not add cloud deployment by default.
- Do not hardcode credentials.
- Do not do unrelated refactors.
