import React from 'react';
import './App.css';
import PopupPage from "./Popup.js";
import OptionsPage from "./Options.js";

function App() {

  function isPopup() {
    var url = window.location.search.substring(1);
    return (url.split('=')[1] === 'true');
  }

  return (
    <div className="App">
      {isPopup() ? (
        <PopupPage />
      ) : (
        <OptionsPage />
      )}
    </div>
  );
}

export default App;
