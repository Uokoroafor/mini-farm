import os


class Settings:
    COLLECTION_NAME: str= "todo_lists"
    USER_COLLECTION_NAME: str="users"
    MONGODB_URI: str= os.environ.get("MONGODB_URI")
    SECRET_KEY: str= os.environ.get("SECRET_KEY")
    ALGORITHM:str = os.environ.get("ALGORITHM","HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES",30)
    DEBUG_MODE: bool =os.getenv("DEBUG", "True").lower() == "true"
    DATABASE_NAME: str=os.environ.get("DATABASE_NAME")
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8080))
    WORKERS: int = int(os.getenv("WORKERS", 2))  # Uvicorn workers - will default to 1 if in debug mode

settings=Settings()