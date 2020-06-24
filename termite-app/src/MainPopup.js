import React from 'react';
import './MainPopup.css';
import IconAndTextItem from './IconAndTextItem.js';


function MainPopup(props) {
	return (
		<div className="MainPopup">
		  
		  
		  <h1>Termite</h1>

			
		  <button id ="MainPopup-grade">
				A+
		  </button>

		  <h2>titlelater</h2>
		  <div id ='MainPopup-reducedsummary'>
			  <IconAndTextItem text="item 1" color="#004d00" />
			  <IconAndTextItem text="item 2" color="#FDA50F" />
			  <IconAndTextItem text="item 3" color="#FF0000" />

			</div>
			<button id='MainPopup-seemore' onClick={() => {props.setPage("Breakdown")}}>
			<p>see more details...</p>
			</button>
		  
		  <div id ="MainPopup-otherlinks">
			
			<button className='MainPopup-link-button' onClick={() => {props.setPage("PolicyHygiene")}}>View my policy hygiene</button>
			<button className='MainPopup-link-button'>View my agreements</button>
			<button className='MainPopup-link-button'>Preferences</button>
			<button className='MainPopup-link-button'>About Termite</button>


	
			</div>


		</div>
	)
}

export default MainPopup;