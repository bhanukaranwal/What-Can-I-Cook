from typing import Optional
from sqlmodel import SQLModel, Field

class FavoriteRecipe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    source_url: str
    image_url: Optional[str] = None
    ingredients: str  # comma-separated list
    instructions: Optional[str] = None
