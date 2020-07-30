/*global chrome*/


import React, {useState, useEffect} from 'react';
import './App.css';
import PopupPage from "./Popup.js";
import OptionsPage from "./Options.js";


function App() {

  const [optionsPage, setOptionsPage] = useState("UserReports");
  const [userID, setUserID] = useState("Jen Jen Jen");
  const [websiteURL, setWebsiteURL] = useState("http://www.testtesttest.com");




  function isPopup() {
    var url = window.location.search.substring(1);
    return (url.split('=')[1] === 'true');
  }

 // chrome.tabs.onUpdated.addListener(function(id, info, tab){
   //const tabURL = tab.url;
  // setWebsiteURL(tabURL);
  //});

//  useEffect(() => {
//    chrome.identity.getProfileUserInfo(function(info){
//      setUserID(info.email);
 //     console.log(info);
 //   });
 // }, [setUserID]);

  return (
    <div className="App">
      {isPopup() ? (
        <PopupPage userID={userID} websiteURL={websiteURL}/>
      ) : (
        <OptionsPage userID={userID} websiteURL={websiteURL} page={optionsPage} setPage={setOptionsPage}/>
      )}
    </div>
  );
}

export default App;
