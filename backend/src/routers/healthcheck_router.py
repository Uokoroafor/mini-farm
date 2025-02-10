from datetime import datetime
from bson import ObjectId
from fastapi import APIRouter, Request, HTTPException
from schemas.todo_schemas import HealthCheckResponse

router = APIRouter(prefix="/health")


@router.get("/")
async def healthcheck(request: Request) -> HealthCheckResponse:
    try:
        # ✅ Access the database from app.state
        db = request.app.state.db
        db.test_db_connection()

        return HealthCheckResponse(
            id=str(ObjectId()),
            status="healthy",
            when=datetime.now(),
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unhealthy: {str(e)}")
