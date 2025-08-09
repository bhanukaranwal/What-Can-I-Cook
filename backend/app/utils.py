from typing import List

def normalize_ingredient(ingredient: str) -> str:
    return ingredient.strip().lower()

def normalize_ingredients_list(ingredients: List[str]) -> List[str]:
    return [normalize_ingredient(i) for i in ingredients]
