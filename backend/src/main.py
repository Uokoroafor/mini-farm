import sys
from config import settings
from fastapi import FastAPI
import uvicorn

from lifecycle import lifespan
from routers.todo_router import router as todo_router
from routers.healthcheck_router import router as healthcheck_router
from routers.users_router import router as users_router
from auth.routers import router as auth_router
from middleware import LoggingMiddleware, setup_cors


app = FastAPI(lifespan=lifespan, debug=settings.DEBUG_MODE)
# Add middleware
setup_cors(app)
app.add_middleware(LoggingMiddleware)

# Register API routers
app.include_router(todo_router, tags=["To-Do Lists"])
app.include_router(healthcheck_router, tags=["Health Check"])
app.include_router(auth_router, tags=["Authorisation"])
app.include_router(users_router, tags=["Users"])


def main(argv=sys.argv[1:]):
    try:
        uvicorn.run(
            "main:app",
            host=settings.HOST,
            port=settings.PORT,
            reload=settings.DEBUG_MODE,
            workers=settings.WORKERS if not settings.DEBUG_MODE else 1,
        )
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
