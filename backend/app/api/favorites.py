from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from .. import models

router = APIRouter()

@router.post("/favorites")
def add_favorite(recipe_id: str, title: str, db: Session = Depends(get_db)):
    fav = models.FavoriteRecipe(id=recipe_id, title=title)
    db.add(fav)
    db.commit()
    return {"message": "Added to favorites"}

@router.get("/favorites")
def list_favorites(db: Session = Depends(get_db)):
    favorites = db.query(models.FavoriteRecipe).all()
    return favorites
