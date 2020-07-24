import React from 'react';

function FunctionalApp({match}) {
	return (
	<div className="App">
		{(match.params.page === "options") ? (
			<div className="OptionsPage">
			  <h1>Termite</h1>

			  <h2>About Our Classifier</h2>

			  <h2>User Preferences</h2>

			  <button>click me</button>

			  <h2>User reports</h2>
			 </div>
		) : (
			<div className="PopupPage">
			  <h1>Termite</h1>

			  <h2>POPOPOPOPUPUPUP</h2>
			</div>
		)}
	</div>
	)
}

export default FunctionalApp;