import openai
import os

class AIRecipeSuggester:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    async def suggest_recipe(self, ingredients: list[str], constraints: str = ""):
        prompt = (
            f"Suggest 3 unique, detailed recipes using only: {', '.join(ingredients)}. "
            f"{constraints} Include name, step-by-step instructions, estimated calories, and cuisine type."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"]
