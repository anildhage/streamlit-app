# Project Overview

This repository is for a local-first Python application that combines:
- Skill training and learning notes.
- Career roadmap tracking.
- Project tracking and resume bullet generation.
- Personal finance tracking using Plaid.
- Todo and goals management.
- Unified dashboards.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd streamlit-app
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run Locally

Start the application:
```bash
streamlit run app.py
```

## Environment Variables

Ensure the following environment variables are set:
- `PLAID_CLIENT_ID`: Your Plaid client ID.
- `PLAID_SECRET`: Your Plaid secret.

## Scripts

- `run`: Start the application.
- `test`: Run tests.

## Project Structure

- `docs/`: Documentation files.
- `prompts/`: Prompt files for AI agents.
- `README.md`: Project overview.

## Troubleshooting

If you encounter issues, ensure all dependencies are installed and environment variables are correctly set.