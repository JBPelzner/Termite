import React, {useState} from 'react';
import "./UserPreferencesOptions.css";
import PreferencesSliderSub from './PreferencesSliderSub.js';
import PreferencesSlider from "./PreferencesSlider.js";

function UserPreferencesOptions() {
	return (
		<div className="UserPreferencesOptions">
			<div className="UserPreferencesOptions-Header">

				<h2 className="optionsh2">My Preferences</h2>
			  
				<div id="PreferencesBox">

					In order to provide streamlined results, notifications, and personalized scores, we ask that
				you provide us your privacy priorities.  

				Please rate the following topics on their importance to you.

				</div>

			</div>

			<div className="UserPreferencesOptions-Content">

			  	<PreferencesSlider title='Data Collection & Usage' description='This is where we will describe a bit about the topic. Briefly.'/>
			  	
						
			  	<PreferencesSlider title='Cookie Policy (& other forms of tracking)'  description='This is where we will describe a bit about the topic. Briefly.'/>
			  

			  	<PreferencesSlider title='Information Sharing & Selling'  description='This is where we will describe a bit about the topic. Briefly.'/>
			  	

			  	<PreferencesSlider title='Data Deletion & Retention'  description='This is where we will describe a bit about the topic. Briefly.'/>
		
			  	<PreferencesSlider title='Notification of Policy Changes'  description='This is where we will describe a bit about the topic. Briefly.'/>
			  	
			  

			  	<PreferencesSlider title='Censorship & Suspension Policy'  description='This is where we will describe a bit about the topic. Briefly.'/>
			  	

			</div>

			<button> Save Preferences </button>
		</div>
	)
}

export default UserPreferencesOptions;