import React from 'react';
import Header from "./components/Header.js";
import Home from './pages/home.jsx';
import Pages from './pages/pages.jsx';
import "./App.css";
{/*import AddIngredient from "./AddIngredient";
import SeeDates from "./SeeDates";
import IngredientList from "./IngredientList";*/}

function App() {
  return (
    <div>
      <Home />
      <Pages />
      {/*<AddIngredient />
      <IngredientList />
  <SeeDates />*/}
    </div>  
  )
};

export default App;