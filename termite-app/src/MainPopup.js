import React, {useState} from 'react';
import './MainPopup.css';
import IconAndTextItem from './IconAndTextItem.js';


function MainPopup(props) {

	const [scores, setScores] = useState([]);

	fetch('http://ec2-18-188-128-88.us-east-2.compute.amazonaws.com:3005/data/model?website_address=http://www.testtesttest.com', {
		method: "GET",
		headers: {"Content-Type": "application/json"}
	})
	.then(res => res.json())
	.then(data => {
		setScores(data[0]);
	})
	.catch(err => console.log(err));

	function generateSubScores() {
		var avg_scores = [];
		const score_tuples = Object.entries(scores);

		["sub1", "sub2", "sub3", "sub4", "sub5", "sub6"].forEach(sub_str => {
			var topic_score = 0;
			var subtopic_count = 0;
			score_tuples.forEach(tuple=>{
				if (sub_str === tuple[0].slice(0,4)){
					if(tuple[0].slice(-5) === "score"){
						topic_score += tuple[1];
						subtopic_count += 1;
					}
				}
			});

			avg_scores.push(topic_score/subtopic_count);
			

		});

		const names =["Censorship & Suspension Policy", 
						"Data Deletion & Retention", 
						"Cookie Policies & Other Tracking", 
						"Data Collection & Usage", 
						"Information Sharing & Selling", 
						"Policy Changes & Notifications"];
		var html_items = [];
		var loopcount = 0;
		avg_scores.forEach(score => {

			var name = names[loopcount];

			html_items.push(
				<IconAndTextItem 
					text={name}
					score={score}
					color="#004d0080"
				/>
			);

			loopcount += 1;
		});
		
				
			
		return html_items;
	}

	return (
		<div className="MainPopup">
		
		  <button id ="MainPopup-grade">
				A+
		  </button>
		


		  <div className="subheader">
		  	<h2 id="MainPopup-Summary">Summary</h2>
		  </div>
		  <div id ='MainPopup-reducedsummary'>
		  	{generateSubScores()}

			</div>

		  
		  <div className="subheader">
		  	<h2 id="MainPopup-Actions">Actions</h2>
		  </div>

		  <div id ="MainPopup-otherlinks">
			
			<button className='Popup-link-button' onClick={() => {
				props.setPage("PolicyHygiene");
				props.setTitle("Policy Hygiene");
			}}>View my policy hygiene</button>
			<button className='Popup-link-button'>View my agreements</button>
			<button className='Popup-link-button' onClick={() => {
				props.setPage("Preferences");
				props.setTitle("My Preferences");
			}}>Preferences</button>
			<button className='Popup-link-button'>About Termite</button>


	
			</div>


		</div>
	)
}

export default MainPopup;