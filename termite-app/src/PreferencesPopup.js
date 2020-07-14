import React from 'react';
import './MainPopup.css';
import './PreferencesPopup.css';
import IconAndTextItem from './IconAndTextItem.js';
import PreferencesSliderSub from './PreferencesSliderSub.js';
import PreferencesSlider from "./PreferencesSlider.js";

function PreferencesPopup(props) {
	return (
		<div className="PreferencesPopup">

		  <div id="PreferencesBox">

		  	<p id='PreferencesPopup-Text'>
				
				In order to provide streamlined results, notifications, and personalized scores, we ask that
				you provide us your privacy priorities.  

				Please rate the following topics on their importance to you.
				</p>

				<div id='PreferencesScrollbox'>

			  	<PreferencesSlider title='Data Collection & Usage' description='This is where we will describe a bit about the topic. Briefly.'/>
			  	
						
			  	<PreferencesSlider title='Cookie Policy (& other forms of tracking)'  description='This is where we will describe a bit about the topic. Briefly.'/>
			  

			  	<PreferencesSlider title='Information Sharing & Selling'  description='This is where we will describe a bit about the topic. Briefly.'/>
			  	

			  	<PreferencesSlider title='Data Deletion & Retention'  description='This is where we will describe a bit about the topic. Briefly.'/>
		
			  	<PreferencesSlider title='Notification of Policy Changes'  description='This is where we will describe a bit about the topic. Briefly.'/>
			  	
			  

			  	<PreferencesSlider title='Censorship & Suspension Policy'  description='This is where we will describe a bit about the topic. Briefly.'/>
			  	

			  	
				

				</div>

			</div>

		  <div id="EditInfoBox">
		
		 	</div>



		</div>
	)
}

export default PreferencesPopup;