import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./recipes.db")
CACHE_TTL_SECONDS = int(os.getenv("CACHE_TTL_SECONDS", 3600))
THEMEALDB_BASE = os.getenv("THEMEALDB_BASE", "https://www.themealdb.com/api/json/v1/1")
SPOONACULAR_KEY = os.getenv("SPOONACULAR_KEY")
EDAMAM_APP_ID = os.getenv("EDAMAM_APP_ID")
EDAMAM_APP_KEY = os.getenv("EDAMAM_APP_KEY")
REDIS_URL = os.getenv("REDIS_URL")
APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
APP_PORT = int(os.getenv("APP_PORT", 8000))
