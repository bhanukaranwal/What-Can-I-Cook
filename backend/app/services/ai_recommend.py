import openai
import os

class AIRecipeSuggester:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    async def suggest_recipe(self, ingredients: list[str]):
        prompt = f"Suggest 3 creative recipes using only: {', '.join(ingredients)}. Include name, steps, and approximate calories."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"]
