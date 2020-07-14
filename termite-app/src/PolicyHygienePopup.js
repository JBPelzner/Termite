import React from 'react';
import './MainPopup.css';
import './PolicyHygienePopup.css';
import IconAndTextItem from './IconAndTextItem.js';
import Backarrow from './backarrow.png';

function PolicyHygienePopup(props) {
	return (
		<div className="PolicyHygienePopup">
		  

		  <div id="PolicyHygiene-MainViz">
			// visualizations go here //
		 	</div>

		  
		  <div id='PolicyHygienePopup-links'>
		  <button className='Popup-link-button'>View my full policy hygiene report</button>
			<button className='Popup-link-button'>View my agreements</button>
			<button className='Popup-link-button' onClick={() => {
				props.setPage("Preferences");
				props.setTitle("My Preferences");
			}}>Edit Preferences</button>

		  </div>



		</div>
	)
}

export default PolicyHygienePopup;