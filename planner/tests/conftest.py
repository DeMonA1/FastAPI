import asyncio

from httpx import AsyncClient, ASGITransport
import pytest_asyncio

from main import app
from database.connection import Settings
from models.events import Event
from models.users import User
    

async def init_db():
    test_settings = Settings()
    test_settings.DATABASE_URL = "mongodb://localhost:27017/testdb"
    
    await test_settings.initialize_database()
    

@pytest_asyncio.fixture(loop_scope="session", scope="session")
async def default_client():
    await init_db()
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://app") as client:
        yield client
        # Clean up resources
        await Event.find_all().delete()
        await User.find_all().delete()