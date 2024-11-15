from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional, Any, List
from pydantic import BaseSettings, BaseModel
from models.users import User
from models.events import Event


class Settings(BaseSettings):
    DATABASE_URL: Optional[str]

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(), document_models=[Event, User])

    class Config:
        env_file = ".venv"
