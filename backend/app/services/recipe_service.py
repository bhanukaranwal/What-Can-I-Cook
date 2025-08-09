from typing import List, Dict
from ..providers.themealdb import TheMealDBProvider
from ..providers.spoonacular import SpoonacularProvider
from .cache import SimpleCache

cache = SimpleCache(ttl=600)
mealdb_provider = TheMealDBProvider()
spoonacular_provider = SpoonacularProvider()

async def get_recipes_from_ingredients(ingredients: List[str]) -> List[Dict]:
    cache_key = ",".join(sorted(ingredients))
    cached = cache.get(cache_key)
    if cached:
        return cached

    results = []
    providers = [mealdb_provider, spoonacular_provider]

    for provider in providers:
        try:
            data = await provider.search_by_ingredients(ingredients)
            results.extend(data)
        except Exception as e:
            print(f"Provider {provider.__class__.__name__} failed: {e}")

    # Remove duplicates by ID and title
    unique = { (r['id'], r['title']): r for r in results }
    final_results = list(unique.values())

    cache.set(cache_key, final_results)
    return final_results
