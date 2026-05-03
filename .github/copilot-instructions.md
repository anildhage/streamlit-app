# Copilot instructions for this repository

## Project overview
- This project is a Python Streamlit app.
- The app loads data from CSV files and external APIs.
- It transforms and combines data with pandas.
- It displays outputs in Streamlit using tables, filters, metrics, and charts.

## Technical preferences
- Use Python and Streamlit-native patterns first.
- Use pandas for tabular transformations.
- Prefer Plotly for interactive charts shown in Streamlit.
- Prefer requests or the existing HTTP client already used in the repo for API calls.
- Use type hints for new functions when practical.

## Architecture
- Keep UI code separate from data loading and transformation logic.
- Put reusable data-access code in helper/service modules.
- Put reusable transformation code in dedicated functions.
- Keep Streamlit page files focused on layout, user inputs, and display logic.

## Data handling
- Validate expected columns after loading CSV files.
- Handle missing values, empty DataFrames, duplicate rows, and schema drift safely.
- Normalize column names when helpful.
- Make transformations explicit and easy to review.
- Avoid mutating shared DataFrames unexpectedly; copy when needed.

## API handling
- Add timeout values to API requests.
- Handle network errors, bad status codes, and malformed responses.
- Parse API responses into predictable tabular structures before sending to the UI.
- Keep secrets and API keys out of source code; use environment variables or Streamlit secrets.

## Streamlit behavior
- Use st.cache_data for deterministic data-loading or transformation steps when helpful.
- Use st.session_state for user-driven state across interactions.
- Show friendly empty states, loading states, and error messages in the UI.
- Keep the app responsive for large datasets; avoid unnecessary recomputation.

## Code quality
- Write small functions with clear names.
- Prefer readable code over clever code.
- Add docstrings for non-trivial functions.
- When generating code, follow existing project structure and dependencies.
- Do not introduce heavy new dependencies unless clearly justified.

## Output expectations
- When adding a feature, include:
  - data loading/update logic,
  - validation/error handling,
  - Streamlit display code,
  - and any needed helper functions or tests if the repo already uses tests.
