import React, {useState} from 'react';
import './Popup.css';
import MainPopup from './MainPopup.js';
import PolicyHygienePopup from './PolicyHygienePopup.js';

function Popup() {

	const [page, setPage] = useState("Main");

	return (
		<div className="Popup">
		
			{(page === "Main") && <MainPopup setPage={setPage}/> }

			{(page === "PolicyHygiene") && <PolicyHygienePopup setPage={setPage}/> }

		</div>
	)
}

export default Popup;