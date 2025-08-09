import httpx
from typing import List, Dict, Any
from ..config import SPOONACULAR_KEY
from ..utils import normalize_ingredients_list

class SpoonacularProvider:
    BASE_URL = "https://api.spoonacular.com/recipes/findByIngredients"

    async def search_by_ingredients(self, ingredients: List[str]) -> List[Dict[str, Any]]:
        if not SPOONACULAR_KEY:
            return []
        ing_str = ",".join(normalize_ingredients_list(ingredients))
        params = {
            "ingredients": ing_str,
            "number": 10,
            "apiKey": SPOONACULAR_KEY
        }
        async with httpx.AsyncClient() as client:
            resp = await client.get(self.BASE_URL, params=params)
            resp.raise_for_status()
            data = resp.json()
            return [
                {
                    "id": str(item["id"]),
                    "title": item["title"],
                    "image_url": item.get("image"),
                    "source": "Spoonacular"
                }
                for item in data
            ]
