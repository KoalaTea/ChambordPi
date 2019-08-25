import React from "react";
import "./App.css";
import Menu from "./Menu";

const App: React.FC = () => {
  return (
    <div className="App">
      <header className="App-header">
        <p>Basic stuff for basic people</p>
        <Menu />
      </header>
    </div>
  );
};

export default App;
