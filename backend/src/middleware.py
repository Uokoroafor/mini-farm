from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import time


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        print(
            f"Request {request.method} {request.url} completed in {process_time:.2f}s"
        )
        return response


def setup_cors(app: FastAPI):
    # Enable CORS for frontend access
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
            "http://0.0.0.0:5173",
            "http://localhost:8000",
            "http://0.0.0.0:8000",
            "http://localhost:80",
            "http://0.0.0.0:80",
            "http://frontend:5173",
            "http://localhost:3001",
            "http://0.0.0.0:3001",
        ],
        # allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
