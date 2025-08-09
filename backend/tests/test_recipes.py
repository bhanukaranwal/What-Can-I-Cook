import pytest
from httpx import AsyncClient
from backend.app.main import app

@pytest.mark.asyncio
async def test_search_recipes():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/recipes", params={"ingredients": ["chicken", "rice"]})
    assert response.status_code == 200
    data = response.json()
    assert "recipes" in data
    assert isinstance(data["recipes"], list)
