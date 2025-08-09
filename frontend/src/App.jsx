import React, { useState } from 'react';
import axios from 'axios';

export default function App() {
  const [ingredients, setIngredients] = useState('');
  const [recipes, setRecipes] = useState([]);

  const searchRecipes = async () => {
    try {
      const res = await axios.get('/api/recipes', {
        params: { ingredients: ingredients.split(',').map(i => i.trim()) }
      });
      setRecipes(res.data.recipes);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="app">
      <h1>What Can I Cook?</h1>
      <input
        type="text"
        value={ingredients}
        onChange={(e) => setIngredients(e.target.value)}
        placeholder="Enter ingredients, separated by commas"
      />
      <button onClick={searchRecipes}>Search</button>
      <div className="recipes">
        {recipes.map((r) => (
          <div key={r.id} className="recipe-card">
            <img src={r.image} alt={r.title} />
            <h3>{r.title}</h3>
          </div>
        ))}
      </div>
    </div>
  );
}
