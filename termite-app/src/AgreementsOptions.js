import React, {useState, useEffect} from 'react';
import "./AgreementsOptions.css";

import {getUserAgreements} from "./utils/ApiCalls.js";

function AgreementsOptions(props) {

	const [agreements, setAgreements] = useState([]);

	useEffect(() => {
		getUserAgreements(props.userID)
		.then(data => {
			setAgreements(data);
		});
	}, [props.userID, setAgreements]);

	function generateAgreementsTable() {
		var tbl = [];
		var i = 0;
		agreements.forEach(agreement => {
			tbl.push(
				<tr key={i}>
					<td>
						<p>{agreement.website_url}</p>
					</td>
					<td>
						<p>(Ex) Website Name Here</p>
					</td>
					<td>
						<p>(Ex) Website Total Score Here</p>
					</td>
					<td>
						<p>(Ex) Website Reliability Here</p>
					</td>
					<td>
						<p>(Ex) Website Accessibility Here</p>
					</td>
				</tr>
			);
			i += 1;
		});
		return tbl;
	}

	return (
		<div className="AgreementsOptions">
			<div className="AgreementsOptions-Header">
				<h2 className="optionsh2">My User Agreements</h2>
			</div>
			<div className="AgreementsOptions-Content">
				<div className="AgreementsOptions-ContentInner">
					<table className="AgreementsOptions-Table">
						<tbody>
							{generateAgreementsTable()}
						</tbody>
					</table>
				</div>
			</div>
		</div>
	)
}

export default AgreementsOptions;