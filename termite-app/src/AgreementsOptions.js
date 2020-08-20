import React, {useState, useEffect} from 'react';
import "./AgreementsOptions.css";
import 'react-tabulator/lib/styles.css'; // required styles
import 'react-tabulator/lib/css/tabulator.min.css'; // theme
import { ReactTabulator } from 'react-tabulator'; // for React 15.x, use import { React15Tabulator }
import {getUserAgreementsFrontend} from "./utils/ApiCalls.js";

function AgreementsOptions(props) {

	const [agreements, setAgreements] = useState([]);


	const columns = [
  { title: 'Website', field: 'website_url', width: 100,  sorter:"alphanum" },
  { title: 'Date of Terms Update', field: 'date_terms_update', width: 100,hozAlign: 'left', formatter: 'date' },
  { title: 'Total Score', field: 'total_score',formatter:'progress' },
  { title: 'Censorship & Suspension Policy', field: 'topic1_score', formatter:'progress' },
  { title: 'Data Deletion & Retention', field: 'topic2_score', formatter:'progress' },
  { title: 'Cookie Policies & Other Tracking', field: 'topic3_score',formatter:'progress' },
  { title: 'Data Collection & Usage', field: 'topic4_score', formatter:'progress' },
  { title: 'Information Sharing & Selling', field: 'topic5_score', formatter:'progress' },
  { title: 'Policy Changes & Notifications', field: 'topic6_score', formatter:'progress' },
  { title: 'Public Accessibility Score', field: 'lexicon_score', formatter: 'star'  },

];


	const options = {
      movableRows: true,
      initialSort: 'date',
      pagination: true,
      paginationSize: '20',
      resizableRows: true,
      resizableColumns: true,
      columnMinWidth:'80',
      layoutColumnsOnNewData: true,




    };


	function generateSubScores(rawdata) {
			rawdata.forEach(row => {
				var avg_scores = [];
				const score_tuples = Object.entries(row);
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

		var i = 1
		avg_scores.forEach(topic => {
			
			if (i === 1){
				var key = 'topic1_score';
			}
			if (i === 2){
				var key = 'topic2_score';
			}
			if (i === 3){
				var key = 'topic3_score';
			}
			if (i === 4){
				var key = 'topic4_score';
			}
			if (i === 5){
				var key = 'topic5_score';
			}
			if (i === 6){
				var key = 'topic6_score';
			}

			row[key] = topic;
			i+=1
				});
		row['total_score'] = avg_scores[0] + avg_scores[1] + avg_scores[2] + avg_scores[3] + avg_scores[4] + avg_scores[5] / 6
	});});
		console.log(rawdata)
		return rawdata
	}



	useEffect(() => {
		getUserAgreementsFrontend(props.userID)

		.then(data => {
			setAgreements(generateSubScores(data));
		});
	}, [props.userID, setAgreements]);


	return (
		<div className="AgreementsOptions">
				
			<div className="AgreementsOptions-Content">

			<h2 className="optionsh2">My Agreements</h2>
			
			<p id="AgreementsCaption"> Here’s a detailed record of your user agreements. This information is visible only to you.</p>
				<div id ='AgreementsTable'>
				<ReactTabulator columns={columns} data={agreements} options={options} />
				</div>
				
		
			</div>
		</div>
	)
}

export default AgreementsOptions;