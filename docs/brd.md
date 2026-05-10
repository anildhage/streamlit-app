# Business Requirements Document: Personal Growth, Career, Finance, and Productivity Platform

## Overview
This document defines the business requirements for a local-first Python application that combines developer skill training, career planning, automated resume building, personal finance tracking, productivity management, and unified dashboards. The application is intended to run locally first, with architecture choices that can later support cloud deployment if needed. The solution should also serve as a hands-on learning vehicle for GitHub Copilot, including end-to-end use of Copilot chat, inline completions, agent mode in the IDE, and Copilot coding agent workflows available under GitHub Copilot Pro.[1][2][3]

## Business Context
The application is meant to solve a fragmented personal workflow problem: learning is tracked in one place, projects in another, finance data elsewhere, and career progress often remains undocumented. A unified local platform would allow continuous capture of work, learning, outcomes, and goals so that progress can be translated directly into insight, planning, and resume-ready achievements. FastAPI supports larger modular applications with separated routers and modules, which aligns well with this multi-domain product scope.[4][5]

A secondary business objective is AI-assisted development capability building. GitHub Copilot Pro is priced at $10 per month and includes unlimited completions plus access to Copilot Chat, Copilot cloud agent, and a monthly allowance of premium requests, making it suitable as the main AI development companion for this project.[6][7][1]

## Product Vision
The product should act as a personal operating system for growth and execution. It should help the user learn technical skills, capture project outcomes, build a career roadmap, track bank transactions, manage tasks and goals, and view all signals in one dashboard. Streamlit is intended for fast internal app experiences and data-app style interfaces, while FastAPI and SQL database patterns support structured CRUD and modular service layers.[5][8][9]

## Objectives
- Provide a single local application for learning, career planning, productivity, and finance management.[9]
- Reduce manual documentation by capturing insights, project outcomes, and resume bullets as work happens.[10]
- Track banking transactions through Plaid and store normalized transaction data for later analysis.[11]
- Enable structured CRUD operations across all major entities, including skills, projects, notes, roadmap items, goals, todos, accounts, and transactions.[5]
- Offer dashboard views that summarize progress, finances, and work in one place.[8][9]
- Use the project as a practical environment to learn GitHub Copilot features end to end, including autonomous and agentic workflows.[2][3][12]

## In Scope
- Local-first web application built with a Python stack.[4][5]
- FastAPI backend with modular routes, schemas, models, and services.[4]
- Streamlit frontend for forms, CRUD screens, dashboards, and internal workflows.[8][9]
- Database storage using SQLite initially, with future portability to PostgreSQL.[9][5]
- Skill training workspace to track topics, exercises, code snippets, notes, and insights.
- Career roadmap module to track long-term trajectory, target roles, milestones, learning plans, and evidence of progress.
- Project log module to track projects, business value, outcomes, impact metrics, and reusable resume bullets.
- Resume builder module to generate resume-ready content from project data.
- Plaid integration for account linking, transaction ingestion, and incremental sync using modern transactions sync patterns.[11]
- Todo and goals management with CRUD support and summary views.
- Unified dashboards across learning, finance, productivity, and career domains.
- GitHub Copilot-enabled development workflow with deliberate usage of chat, completions, agent mode, and coding agent features available to the selected plan.[3][1][2]

## Out of Scope
- Native mobile apps.
- Multi-tenant SaaS deployment in the initial phase.
- Advanced team collaboration features.
- Payroll, tax filing, or full accounting workflows.
- Production-grade banking operations beyond Plaid-based data ingestion and analysis.
- Public-facing resume website in phase one.
- Full autonomous production deployment pipelines during the first local build phase.

## Users and Stakeholders
### Primary User
- Individual technical professional building a personal system for learning, planning, finance tracking, and execution.

### Key Stakeholder Goals
- Learn while building.
- Reduce administrative overhead around resume updates and career tracking.
- Centralize project evidence and quantified value creation.
- Create a foundation for future analytics and automation.
- Learn practical AI-assisted software delivery using GitHub Copilot Pro capabilities.[1][2][3]

## Functional Requirements
### 1. Skill Training and Insight Capture
- The system shall allow creation of skill domains such as Python, SQL, cloud, AI tools, or any user-defined topic.
- The system shall allow entry of practice sessions, exercises, code snippets, prompts used, learning notes, and insights.
- The system shall support tagging, searching, filtering, and status tracking for learning items.
- The system shall allow linking skill items to projects, roadmap milestones, or resume evidence.

### 2. Career Roadmap
- The system shall allow definition of target roles, timelines, required competencies, milestones, and gap assessments.
- The system shall allow progress tracking over time with notes, proof points, and linked artifacts.
- The system shall show a career trajectory view with current position, next target, dependencies, and readiness indicators.

### 3. Project and Resume Engine
- The system shall allow users to create and update project records with title, description, technologies, dates, business value, metrics, and outcomes.
- The system shall support capturing impact in quantified form, such as time saved, automation created, or process improvement.
- The system shall derive draft resume bullets from project records and append them to a resume repository for later refinement.
- The system shall support marking certain bullets as approved, draft, or archived.
- The system shall support exporting resume content in a structured format for later document generation.

### 4. Finance Tracking via Plaid
- The system shall allow secure Plaid-based account linking for supported institutions.[11]
- The system shall ingest bank accounts and transactions into local storage.
- The system shall use incremental transaction synchronization rather than repeated full loads where supported.[11]
- The system shall support categorization, merchant views, date filters, account summaries, and trend analysis.
- The system shall preserve transaction history and support downstream analytics queries.

### 5. CRUD Administration
- The system shall support create, read, update, and delete operations for all core entities.[5]
- The system shall support audit-friendly timestamps such as created_at and updated_at.
- The system shall support soft delete for records where history should be preserved.

### 6. To-Do and Goals Management
- The system shall allow CRUD for todos, goals, sub-goals, priorities, due dates, and statuses.
- The system shall support summarized views such as overdue items, in-progress items, completed milestones, and weekly snapshots.
- The system shall allow linking todos and goals to projects, skill items, and roadmap milestones.

### 7. Unified Dashboard
- The system shall show a consolidated home view with learning progress, roadmap milestones, project activity, resume updates, finance snapshots, and goal summaries.
- The system shall support filtered dashboards by time period, domain, and status.
- The system shall surface insights such as top spending categories, active learning themes, stalled roadmap items, and recent impact captured.

## Non-Functional Requirements
- The application shall run locally on a developer machine as the primary deployment model in phase one.
- The application shall be built using a Python-first stack, with FastAPI for backend services and Streamlit for the UI layer.[8][4]
- The application shall use a relational database, beginning with SQLite and preserving a clean migration path to PostgreSQL.[9][5]
- The architecture shall follow modular application patterns suitable for larger FastAPI projects.[4]
- Sensitive credentials such as Plaid keys shall be stored in environment variables, not hardcoded.
- The system shall support maintainable code organization, testability, and future extension.
- The system should remain usable offline for non-Plaid workflows once local data has been stored.

## Proposed Solution Architecture
### Application Layer
- Streamlit frontend for dashboards, data entry, forms, review screens, and admin workflows.[8][9]
- FastAPI backend for APIs, business logic orchestration, validation, services, and integration endpoints.[5][4]

### Data Layer
- SQLAlchemy ORM models and Alembic migrations for schema evolution, following FastAPI database patterns.[5]
- SQLite as initial local database, with schema discipline compatible with a later PostgreSQL move.[9][5]

### Integration Layer
- Plaid integration service for link, token exchange, account retrieval, and incremental transactions sync.[11]
- Background sync jobs or scheduled tasks for regular transaction refresh.

### Domain Modules
- Skills.
- Career roadmap.
- Projects.
- Resume bullets and resume exports.
- Goals.
- Todos.
- Accounts and transactions.
- Dashboard and reporting.

## Key Workflows
### Learning Workflow
1. Create a skill topic.
2. Add practice notes and code insights after each session.
3. Link learning to a project or career milestone.
4. Review progress in dashboard form.

### Project-to-Resume Workflow
1. Create or update a project.
2. Capture business value and metrics.
3. Generate draft resume bullets.
4. Review and approve selected bullets.
5. Export approved resume entries for final resume assembly.

### Finance Workflow
1. Link financial account through Plaid.[11]
2. Sync accounts and transactions to local database.[11]
3. Normalize and categorize transactions.
4. Review trends and insights in dashboard views.

### Productivity Workflow
1. Add todos and goals.
2. Update statuses over time.
3. Review summaries and overdue items.
4. Correlate activity with roadmap progress.

## Success Criteria
- All core modules can be used locally from a single application entry point.
- A new project can be captured once and reused in dashboard, roadmap, and resume contexts.
- Plaid transactions can be synced and queried locally using stored data.[11]
- The user can update todos, goals, skills, and projects through simple CRUD screens.[5]
- The application demonstrates clear learning value for GitHub Copilot across the software development lifecycle.[12][2][3]

## Risks and Constraints
- Plaid integration adds external dependency, credential management, and edge-case handling around transaction availability and sync behavior.[11]
- Resume bullet quality may require manual editorial review even if draft generation is automated.
- Streamlit is fast for internal tools, but very custom UX patterns may later favor a dedicated front-end framework.[8]
- Copilot feature availability and billing are evolving, with GitHub moving plans toward usage-based billing beginning June 1, 2026, while base plan pricing remains unchanged.[13][6][1]

## GitHub Copilot Learning Goals for This Project
The project should deliberately use Copilot as both a coding assistant and a learning aid. GitHub documents that Copilot Pro includes unlimited completions, Copilot Chat access, and Copilot cloud agent access, while GitHub also distinguishes between agent mode in the IDE and the cloud-based coding agent that works asynchronously on tasks and pull requests.[2][3][1]

The intended Copilot learning goals are:
- Learn when to use inline completions versus chat-based prompting.[2]
- Learn how agent mode in the IDE can propose multi-file changes and terminal commands with user approval.[2]
- Learn how Copilot coding agent can work on issue-driven tasks and produce pull requests for review.[3][12]
- Learn how to structure tasks, prompts, repository context, and documentation so Copilot performs better.[2]
- Learn practical boundaries of AI assistance, including validation, review, security, and human approval steps.[2]

## Phased Delivery Recommendation
### Phase 1: Foundation
- Repository setup.
- FastAPI app structure.
- Database models and migrations.
- Streamlit shell.
- Core CRUD for skills, projects, todos, and goals.[4][8][5]

### Phase 2: Career and Resume
- Career roadmap workflows.
- Project outcomes and impact capture.
- Resume bullet generation and review.
- Dashboard summary integration.

### Phase 3: Finance
- Plaid sandbox setup.
- Account linking and transaction sync.
- Categorization and finance dashboards.[11]

### Phase 4: Copilot Maturity
- Introduce issue-based task planning.
- Add agent mode habits inside the IDE.[2]
- Add coding agent workflows for bounded GitHub issues and PR review loops.[12][3]

## Acceptance Criteria
- Local application starts successfully with documented setup steps.
- User can perform CRUD on core modules from the UI.[5]
- User can link at least one test bank source in Plaid sandbox and retrieve transactions in development mode.[11]
- User can create project records and generate draft resume content from them.
- User can view dashboard summaries across at least learning, productivity, and finance domains.
- Repository structure is clean enough that Copilot can navigate and assist effectively through modular files and explicit task descriptions.[4][2]

