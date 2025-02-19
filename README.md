# 1-Server Flask with React Frontend Example

This is a simple example of a Flask server with a React frontend with Vite. During production, only 1 server (the Flask server) is needed to serve both the frontend and backend. During development, there are 2 servers to enable hot module reloading for the frontend.

## Explanation

The [`index.html`](backend/templates/index.html) file is the entry point for the frontend. During dev mode, the frontend is served by Vite. The Flask app will automatically grab these files from the Vite server so that hot module reloading is enabled. When the frontend is built, the static files are placed in the `backend/build` folder. The Flask server serves the static files from the `backend/build` folder during production.

## Getting Started

1. Clone the repository
2. Create a virtual environment `python -m venv .venv`
3. Activate the virtual environment `source .venv/bin/activate`
4. Install the dependencies `pip install -r requirements.txt`
5. Install the frontend dependencies `cd frontend && npm install`
6. Start the frontend `cd frontend && npm run dev`
7. Start the backend `cd backend && python app.py`
8. Open the browser and go to `http://localhost:8000`
