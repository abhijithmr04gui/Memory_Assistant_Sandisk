# Memory OS – AI Personal Memory Assistant

A memory assistant that stores text memories, embeds them with semantic search (FAISS), and answers questions using retrieved context and Gemini.

## Project structure

```
memory-assistant/
├── backend/          # FastAPI + FAISS + Gemini
│   ├── app/
│   │   ├── api/      # memory_routes, chat_routes
│   │   ├── services/ # embedding, memory, retrieval, llm
│   │   └── vector/   # FAISS index
│   ├── run.py
│   └── requirements.txt
└── frontend/         # React + Vite
    ├── src/
    └── dist/         # Static build output
```

## Backend setup

```bash
cd backend
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Create `.env` in `backend/`:

```
GEMINI_API_KEY=your_gemini_api_key
```

Run:

```bash
cd backend
python run.py
```

Backend runs at `http://127.0.0.1:8000`.

## Frontend setup

### Development

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`.

### Static build (production)

```bash
cd frontend
npm install
npm run build
```

Output: `frontend/dist/` – static HTML, JS, CSS.

To serve locally:

```bash
npm run preview
```

For production, set `VITE_API_URL` to your backend URL before building:

```bash
VITE_API_URL=https://your-api.example.com npm run build
```

Then serve `dist/` with any static host (Nginx, S3, Vercel, etc.).

## Features

- **Store memories** – Add text; memories are embedded and indexed.
- **Ask memories** – Query in natural language; relevant memories are retrieved and used to generate answers.
- **Memory timeline** – View all stored memories in order.
