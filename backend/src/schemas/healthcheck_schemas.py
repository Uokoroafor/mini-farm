from pydantic import BaseModel
from datetime import datetime


class HealthCheckResponse(BaseModel):
    id: str
    status: str
    when: datetime
