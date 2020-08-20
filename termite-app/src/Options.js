import React, {useState} from 'react';
import './Options.css';

import AboutOptions from "./AboutOptions";
import UserPreferencesOptions from "./UserPreferencesOptions";
import UserReportsOptions from "./UserReportsOptions";
import AgreementsOptions from "./AgreementsOptions";


function Options(props) {

	return (
		<div className="Options">
		

			<div className="Options-Nav">
			<div className="Options-Header">
				<h1 class="optionsh1">Termite User Portal</h1>
				</div>

			
				
				{(props.page === "UserReports") ? (
					<button className="Options-NavButtonSelected">My Reports</button>
				) : (
					<button className="Options-NavButton" onClick={() => props.setPage("UserReports")}>My Reports</button>
				)}
				{(props.page === "Agreements") ? (
					<button className="Options-NavButtonSelected">My Agreements</button>
				) : (
					<button className="Options-NavButton" onClick={() => props.setPage("Agreements")}>My Agreements</button>
				)}
				{(props.page === "UserPreferences") ? (
					<button className="Options-NavButtonSelected">Preferences</button>
				) : (
					<button className="Options-NavButton" onClick={() => props.setPage("UserPreferences")}>Preferences</button>
				)}
				{(props.page === "About") ? (
					<button className="Options-NavButtonSelected">About Our Classifier</button>
				) : (
					<button className="Options-NavButton" onClick={() => props.setPage("About")}>About Our Classifier</button>
				)}
				<a href="http://bit.ly/TERMITE"><button className="Options-NavButton">Our Website</button></a>

				<a href="https://odowns3.wixsite.com/termite/contact"><button className="Options-NavButton" >Contact Us</button></a>
			</div>

		<div className="Options-Content">

				{(props.page === "Agreements") && <AgreementsOptions userID={props.userID} /> }
			
				{(props.page === "About") && <AboutOptions /> }

				{(props.page === "UserPreferences") && <UserPreferencesOptions userID={props.userID} /> }

				{(props.page === "UserReports") && <UserReportsOptions /> }

				

			</div>

		</div>
	)
}

export default Options;