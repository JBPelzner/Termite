import React from 'react';
import './MainPopup.css';
import Backarrow from './backarrow.png';


function BreakdownPopup(props) {
	return (
		<div className="BreakdownPopup">
		 
			<input type='image' className='backbutton' src={Backarrow} onClick={() => {props.setPage("Main")}} ></input>
		  
		  <h1>Termite</h1>
		
			
		 

		  <h2>Breakdown</h2>
		  

		</div>
	)
}

export default BreakdownPopup;