import React, {useState, useEffect} from 'react';
import "./UserPreferencesOptions.css";
import PreferencesSliderSub from './PreferencesSliderSub.js';
import PreferencesSlider from "./PreferencesSlider.js";

import {getUserPreferences, postUserPreferences} from "./utils/ApiCalls.js";

function UserPreferencesOptions(props) {

	const [topic1, setTopic1] = useState(4);
	const [topic2, setTopic2] = useState(4);
	const [topic3, setTopic3] = useState(4);
	const [topic4, setTopic4] = useState(4);
	const [topic5, setTopic5] = useState(4);
	const [topic6, setTopic6] = useState(4);
	const [pulled, setPulled] = useState(false);

	useEffect(() => {
		getUserPreferences(props.userID)
		.then(data => {
			if (data.length >= 1) {
				setTopic1(data[0].topic1);
				setTopic2(data[0].topic2);
				setTopic3(data[0].topic3);
				setTopic4(data[0].topic4);
				setTopic5(data[0].topic5);
				setTopic6(data[0].topic6);
				setPulled(true);
			}
		});
	}, [getUserPreferences, props.userID, setTopic1, setTopic2, setTopic3, setTopic4, setTopic5, setTopic6, setPulled]);

	useEffect(() => {
		if (pulled) {
			postUserPreferences(props.userID, topic1, topic2, topic3, topic4, topic5, topic6);
		}
	}, [pulled, props.userID, topic1, topic2, topic3, topic4, topic5, topic6]);


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

			  	<PreferencesSlider 
			  		title='Data Collection & Usage' 
			  		description='This is where we will describe a bit about the topic. Briefly.'
			  		value={topic1}
			  		setValue={setTopic1}
			  	/>
			  	
			  	<PreferencesSlider 
			  		title='Cookie Policy (& other forms of tracking)'  
			  		description='This is where we will describe a bit about the topic. Briefly.'
			  		value={topic2}
			  		setValue={setTopic2}
			  	/>
			  
			  	<PreferencesSlider 
			  		title='Information Sharing & Selling'  
			  		description='This is where we will describe a bit about the topic. Briefly.'
			  		value={topic3}
			  		setValue={setTopic3}	  		
			  	/>

			  	<PreferencesSlider 
			  		title='Data Deletion & Retention'  
			  		description='This is where we will describe a bit about the topic. Briefly.'
			  		value={topic4}
			  		setValue={setTopic4}
			  	/>
		
			  	<PreferencesSlider 
			  		title='Notification of Policy Changes'  
			  		description='This is where we will describe a bit about the topic. Briefly.'
			  		value={topic5}
			  		setValue={setTopic5}
			  	/>
			  	
			  	<PreferencesSlider 
			  		title='Censorship & Suspension Policy'  
			  		description='This is where we will describe a bit about the topic. Briefly.'
			  		value={topic6}
			  		setValue={setTopic6}	
			  	/>

			</div>

		</div>
	)
}

export default UserPreferencesOptions;