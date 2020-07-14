import React from 'react';
import Backarrow from './backarrow.png';
import BreakdownDropdown from './BreakdownDropdown.js';
import './BreakdownPopup.css';


function BreakdownPopup(props) {
	return (
		<div className="BreakdownPopup">
		 
		  <div id='BreakdownPopup-Background'>
		   <BreakdownDropdown text="topic 1" color="#004d00" description="this is a description. look at me go."/>
		   <BreakdownDropdown text="topic 2" color="#004d00" description="this is a description. look at me go."/>
		   <BreakdownDropdown text="topic 3" color="#004d00" description="this is a description. look at me go."/>
		   <BreakdownDropdown text="topic 4" color="#004d00" description="this is a description. look at me go."/>
		   <BreakdownDropdown text="topic 5" color="#004d00" description="this is a description. look at me go."/>
		   <BreakdownDropdown text="topic 6" color="#004d00" description="this is a description. look at me go."/>
		   <BreakdownDropdown text="topic 7" color="#004d00" description="this is a description. look at me go."/>
		   <BreakdownDropdown text="topic 8" color="#004d00" description="this is a description. look at me go."/>
		   <BreakdownDropdown text="topic 9" color="#004d00" description="this is a description. look at me go."/>
		   <BreakdownDropdown text="topic 10" color="#004d00" description="this is a description. look at me go."/>

		  </div>



		</div>
	)
}

export default BreakdownPopup;