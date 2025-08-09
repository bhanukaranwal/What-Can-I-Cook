import React, { useState } from 'react';
import { themes } from '../theme';

export default function ThemeToggle({ onThemeChange }) {
  const [theme, setTheme] = useState('light');

  const toggleTheme = () => {
    const themeKeys = Object.keys(themes);
    const currentIndex = themeKeys.indexOf(theme);
    const nextTheme = themeKeys[(currentIndex + 1) % themeKeys.length];
    setTheme(nextTheme);
    onThemeChange(themes[nextTheme]);
  };

  return (
    <button onClick={toggleTheme}>
      Switch Theme (Current: {theme})
    </button>
  );
}
