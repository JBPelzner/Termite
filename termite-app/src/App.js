import React, {useState} from 'react';
import './App.css';
import PopupPage from "./Popup.js";
import OptionsPage from "./Options.js";

function App() {

  const [optionsPage, setOptionsPage] = useState("About");

  function isPopup() {
    var url = window.location.search.substring(1);
    return (url.split('=')[1] === 'true');
  }

  return (
    <div className="App">
      {isPopup() ? (
        <PopupPage />
      ) : (
        <OptionsPage page={optionsPage} setPage={setOptionsPage}/>
      )}
    </div>
  );
}

export default App;
