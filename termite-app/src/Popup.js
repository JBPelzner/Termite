import React, {useState} from 'react';
import './Popup.css';
import MainPopup from './MainPopup.js';
import PolicyHygienePopup from './PolicyHygienePopup.js';
import BreakdownPopup from './BreakdownPopup.js'
import ToggleButton from 'react-toggle-button'

function Popup() {

	const [operational, toggleOperational] = useState("True");

	const [page, setPage] = useState("Main");

	return (
		<div className="Popup">
		


			<div className='toggleButton-popup'>
				<ToggleButton
				  value={ operational || false }
				  onToggle={(value) => {
				    toggleOperational(!value)
				  }} />
				</div>
			

				{(page === "Main") && <MainPopup setPage={setPage}/> }

				{(page === "PolicyHygiene") && <PolicyHygienePopup setPage={setPage}/> }

				{(page === "Breakdown") && <BreakdownPopup setPage={setPage}/> }

		</div>
	)
}

export default Popup;