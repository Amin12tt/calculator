# Calculator

This is my first project: a simple web calculator built with FastAPI and static HTML/CSS/JavaScript.

## About

This calculator app includes:
- A modern calculator UI in `static/index.html`
- A Python backend API in `calculator.py`
- A simple calculation endpoint at `/api/calc`
- Support for basic arithmetic and exponentiation

## How it works

The frontend sends the math expression to the backend and the backend evaluates it safely.
The app is designed so the UI and the API are served together from one Python application.

## Run locally

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app:
   ```bash
   uvicorn calculator:app --reload --host 0.0.0.0 --port 8000
   ```
4. Open in browser:
   ```
   http://localhost:8000/static/index.html
   ```

## What to expect

- Enter numbers and operators
- Use `+`, `-`, `*`, `/`, and `^` for exponentiation
- Press `=` to calculate
- Errors show when the expression is invalid

## Deployment note

This project needs a backend server because the calculator UI calls `/api/calc`.
That means it cannot be hosted on GitHub Pages alone.

A free cloud host like Render, Railway, or Replit can run this app and provide a public URL.

## My first project

This is my first project with Python web development and a live calculator interface.
It demonstrates how to connect a frontend with a backend API and share the app from GitHub.
