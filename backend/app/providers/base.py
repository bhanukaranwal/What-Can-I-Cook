import abc
from typing import List, Dict, Any

class RecipeProvider(abc.ABC):
    @abc.abstractmethod
    async def search_by_ingredients(self, ingredients: List[str]) -> List[Dict[str, Any]]:
        pass
