What Can I Cook? — Recipe Generator

A modern, feature-rich recipe suggestion platform built with Python (FastAPI) + React, featuring smart ingredient matching, API integrations, AI-powered suggestions, advanced search filters, and beautiful theming.

🚀 Features

Ingredient-based search — Find recipes using what you already have in your kitchen.

Multi-provider support — Integrates with TheMealDB and Spoonacular APIs.

Advanced filters — Cuisine, diet type, max calories, and cooking time.

AI-powered suggestions — Uses GPT to recommend creative recipes.

Favorites management — Save and organize recipes.

Theme customization — Light, dark, and ocean themes with toggle.

Dockerized setup — Easy deployment with Docker and docker-compose.

Full test suite — Unit tests for backend modules.

📂 Repository Structure

.
├── .env.example
├── backend
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── app
│   │   ├── config.py
│   │   ├── utils.py
│   │   ├── db.py
│   │   ├── models.py
│   │   ├── providers
│   │   │   ├── base.py
│   │   │   ├── themealdb.py
│   │   │   ├── spoonacular.py
│   │   ├── services
│   │   │   ├── cache.py
│   │   │   ├── recipe_service.py
│   │   │   ├── ai_recommend.py
│   │   ├── api
│   │   │   ├── endpoints.py
│   │   │   ├── favorites.py
│   │   │   ├── filters.py
│   │   │   ├── main.py
│   │   └── tests
│   │       ├── test_providers.py
│   │       ├── test_services.py
│   │       ├── test_api.py
├── frontend
│   ├── src
│   │   ├── theme.js
│   │   ├── components
│   │   │   ├── ThemeToggle.jsx
│   │   │   ├── RecipeCard.jsx
│   │   │   ├── SearchBar.jsx
│   │   ├── pages
│   │   │   ├── Home.jsx
│   │   │   ├── Favorites.jsx
│   │   │   ├── AdvancedSearch.jsx
│   │   ├── App.jsx
│   │   ├── index.js
├── infra
│   ├── docker-compose.yml

⚙️ Setup & Installation

1️⃣ Clone Repository

git clone https://github.com/yourusername/what-can-i-cook.git
cd what-can-i-cook

2️⃣ Environment Variables

cp .env.example .env

Fill in your API keys for TheMealDB, Spoonacular, and OpenAI.

3️⃣ Docker Setup

docker-compose up --build

Access frontend at http://localhost:3000 and backend API at http://localhost:8000.

🔍 Advanced Search API

GET /recipes/advanced
?ingredients=tomato,cheese
&cuisine=Italian
diet=vegetarian
&max_calories=500
&cooking_time=30

🤖 AI Recipe Suggestions

Using GPT to generate unique, step-by-step recipes:

suggester = AIRecipeSuggester()
recipes = await suggester.suggest_recipe(["tomato", "cheese"], constraints="vegetarian, under 500 calories")

🎨 Themes

Light, dark, and ocean modes with a simple toggle button.

<ThemeToggle onThemeChange={applyTheme} />

🧪 Running Tests

cd backend
pytest

📜 License

MIT License © 2025 Bhanu Karnwal 
