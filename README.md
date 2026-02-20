# Tinder Clone

Deployment on Render.

1.  Fork.
2.  New Web Service.
3.  Build: pip install -r requirements.txt && cd frontend && npm ci && npm run build && cd ..
4.  Start: uvicorn app.main:app --host 0.0.0.0 --port $PORT
5.  Env: DATABASE_URL, SECRET_KEY.

Local:
Backend: uvicorn app.main:app --reload
Frontend: npm start
