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
				<h1 class="optionsh1">Termite</h1>
				</div>

			
				{(props.page === "UserPreferences") ? (
					<button className="Options-NavButtonSelected">User Preferences</button>
				) : (
					<button className="Options-NavButton" onClick={() => props.setPage("UserPreferences")}>Preferences</button>
				)}
				{(props.page === "UserReports") ? (
					<button className="Options-NavButtonSelected">User Reports</button>
				) : (
					<button className="Options-NavButton" onClick={() => props.setPage("UserReports")}>My User Reports</button>
				)}
				{(props.page === "Agreements") ? (
					<button className="Options-NavButtonSelected">Agreements</button>
				) : (
					<button className="Options-NavButton" onClick={() => props.setPage("Agreements")}>Agreements</button>
				)}
				{(props.page === "About") ? (
					<button className="Options-NavButtonSelected">About Our Classifier</button>
				) : (
					<button className="Options-NavButton" onClick={() => props.setPage("About")}>About Our Classifier</button>
				)}

				<button className="Options-NavButton" a href="www.gmail.com">Contact Us</button>
			</div>

		<div className="Options-Content">
			
				{(props.page === "About") && <AboutOptions /> }

				{(props.page === "UserPreferences") && <UserPreferencesOptions /> }

				{(props.page === "UserReports") && <UserReportsOptions /> }

				{(props.page === "Agreements") && <AgreementsOptions /> }

			</div>

		</div>
	)
}

export default Options;