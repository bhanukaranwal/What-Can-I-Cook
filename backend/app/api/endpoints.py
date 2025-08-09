from fastapi import APIRouter, Query
from typing import List
from ..services.recipe_service import get_recipes_from_ingredients

router = APIRouter()

@router.get("/recipes")
async def search_recipes(ingredients: List[str] = Query(...)):
    recipes = await get_recipes_from_ingredients(ingredients)
    return {"count": len(recipes), "recipes": recipes}
