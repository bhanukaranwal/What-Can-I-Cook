import pytest
from httpx import AsyncClient
from backend.app.main import app

@pytest.mark.asyncio
async def test_add_and_list_favorites():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        add_resp = await ac.post("/api/favorites", params={"recipe_id": "123", "title": "Test Dish"})
        assert add_resp.status_code == 200
        assert add_resp.json()["message"] == "Added to favorites"

        list_resp = await ac.get("/api/favorites")
        assert list_resp.status_code == 200
        favorites = list_resp.json()
        assert any(f["title"] == "Test Dish" for f in favorites)
