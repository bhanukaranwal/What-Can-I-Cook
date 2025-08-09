from fastapi import APIRouter, Query
from backend.app.services.recipe_service import RecipeService

router = APIRouter()

@router.get("/recipes/advanced")
async def advanced_search(
    ingredients: list[str] = Query(..., description="List of ingredients"),
    cuisine: str | None = Query(None),
    diet: str | None = Query(None),
    max_calories: int | None = Query(None)
):
    service = RecipeService()
    recipes = await service.get_recipes(ingredients)
    
    if cuisine:
        recipes = [r for r in recipes if cuisine.lower() in (r.get("cuisine") or "").lower()]
    if diet:
        recipes = [r for r in recipes if diet.lower() in (r.get("dietLabels") or "").lower()]
    if max_calories:
        recipes = [r for r in recipes if r.get("calories", 0) <= max_calories]

    return {"recipes": recipes}
