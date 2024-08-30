import httpx
import pytest
import pytest_asyncio

from auth.jwt_handler import create_access_token
from models.events import Event


@pytest_asyncio.fixture(loop_scope="session", scope="session")
async def access_token() -> str:
    return create_access_token("testuser@example.com")


@pytest_asyncio.fixture(loop_scope="session", scope="session")
async def mock_event():
    new_event = Event(
        creator="testuser@example.com",
        title="FastAPI Launch",
        image = "https://unsplash.com/photos/blue-and-green-abstract-painting-Jd09hiCUPCs",
        description = "We will be discussing the contents of the \
                        FastAPI in this event. Ensure to come with \
                        your own copy to win gifts!",
        tags = ["python", "fastapi", "book", "launch"],
        location = "Google Meet")
    
    await Event.insert_one(new_event)
    yield new_event


@pytest.mark.asyncio(loop_scope="session")
async def test_get_events(default_client: httpx.AsyncClient,
                          mock_event: Event) -> None:
    response = await default_client.get("/event/")
    assert response.status_code == 200
    assert response.json()[0]["_id"] == str(mock_event.id)
    

@pytest.mark.asyncio(loop_scope="session")
async def test_post_event(default_client: httpx.AsyncClient,
                          access_token: str) -> None:
    payload = { "title":"FastAPI Launch",
                "image": "https://unsplash.com/photos/blue-and-green-abstract-painting-Jd09hiCUPCs",
                "description": "We will be discussing the contents of the \
                                FastAPI in this event. Ensure to come with \
                                your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"}
    
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {access_token}"}
    
    test_response = {"message": "Event created successfully"}
    
    response = await default_client.post("/event/new", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json() == test_response
    
    
@pytest.mark.asyncio(loop_scope="session")
async def test_get_events_count(default_client: httpx.AsyncClient) -> None:
    response = await default_client.get("/event/")
    events = response.json()
    assert response.status_code == 200
    assert len(events) == 2
    
    
@pytest.mark.asyncio(loop_scope="session")
async def test_update_event(default_client: httpx.AsyncClient,
                            mock_event: Event, access_token: str) -> None:
    test_payload = {"title": "Updated FastAPI event"}
    
    headers = {"Content-Type": "application/json",
                "Authorization": f"Bearer {access_token}"}
    
    url = f"/event/{str(mock_event.id)}"
    response = await default_client.put(url, json=test_payload, headers=headers)
    
    assert response.status_code == 200
    assert response.json()["title"] == test_payload["title"]
    
    
@pytest.mark.asyncio(loop_scope="session")
async def test_delete_event(default_client: httpx.AsyncClient,
                            mock_event: Event, access_token: str) -> None:
    test_response = {"message": "Event deleted successfully."}
    
    headers = {"COntent-Type": "application/json",
               "Authorization": f"Bearer {access_token}"}
    url = f"/event/{mock_event.id}"
    response = await default_client.delete(url, headers=headers)
    
    assert response.status_code == 200
    assert response.json() == test_response
    
    
@pytest.mark.asyncio(loop_scope="session")
async def test_get_event_again(default_client: httpx.AsyncClient,
                               mock_event: Event) -> None:
    url = f"/event/{str(mock_event.id)}"
    response = await default_client.get(url)
    
    assert response.status_code == 404
    
    