import httpx
from typing import List, Dict, Any
from ..config import THEMEALDB_BASE
from ..utils import normalize_ingredient

async def fetch_meals_by_ingredient(ingredient: str) -> List[Dict[str, Any]]:
    url = f"{THEMEALDB_BASE}/filter.php?i={ingredient}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        return resp.json().get("meals", []) or []

class TheMealDBProvider:
    async def search_by_ingredients(self, ingredients: List[str]) -> List[Dict[str, Any]]:
        seen_ids = set()
        results = []
        for ing in ingredients:
            normalized = normalize_ingredient(ing)
            meals = await fetch_meals_by_ingredient(normalized)
            for meal in meals:
                if meal["idMeal"] not in seen_ids:
                    seen_ids.add(meal["idMeal"])
                    results.append({
                        "id": meal["idMeal"],
                        "title": meal["strMeal"],
                        "image_url": meal["strMealThumb"],
                        "source": "TheMealDB"
                    })
        return results
