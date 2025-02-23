from motor.motor_asyncio import AsyncIOMotorClient
from config import settings
from logger import logger


class Database:
    client: AsyncIOMotorClient = None
    db = None

    async def connect(self):
        """Initialise MongoDB connection."""
        if not settings.MONGODB_URI:
            raise Exception("No Mongo DB")
        self.client = AsyncIOMotorClient(settings.MONGODB_URI)
        self.db = self.client[settings.DATABASE_NAME]

        # Initialise Beanie ODM
        # await init_beanie(database=db, document_models=[User])
        logger.info("✅ MongoDB connected.")

    async def close_mongo_connection(self):
        """Close MongoDB connection."""
        if self.client:
            self.client.close()
            logger.info("🛑 MongoDB connection closed.")

    async def test_db_connection(self):
        # Test database availability
        db_ping = await self.db.command("ping")
        if int(db_ping["ok"]) != 1:
            msg = "Connection is not ok."
            logger.error(msg)
            raise Exception(msg)


database = Database()
