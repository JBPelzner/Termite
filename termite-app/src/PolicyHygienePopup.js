import React from 'react';
import './MainPopup.css';
import IconAndTextItem from './IconAndTextItem.js';
import Backarrow from './backarrow.png';

function PolicyHygienePopup(props) {
	return (
		<div className="PolicyHygienePopup">
		  
		  <input type='image' className='backbutton' src={Backarrow} onClick={() => {props.setPage("Main")}} ></input>
		  
		  <h1>Termite</h1>

			
	

		  <h2>policy hygiene</h2>
		  

		  


		</div>
	)
}

export default PolicyHygienePopup;