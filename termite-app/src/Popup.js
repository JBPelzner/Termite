import React, {useState} from 'react';
import './Popup.css';
import MainPopup from './MainPopup.js';
import PolicyHygienePopup from './PolicyHygienePopup.js';
import PreferencesPopup from './PreferencesPopup.js';
import BreakdownPopup from './BreakdownPopup.js';
import ToggleButton from 'react-toggle-button';
import Backarrow from './backarrow.png';

function Popup() {

	const [operational, toggleOperational] = useState("True");

	const [page, setPage] = useState("Main");

	const [title, setTitle] = useState("Termite");

	return (
		<div className="Popup">

			<div className="header" id="MainHeader">

				<h1 id="Termite">{title}</h1>

				<div className='toggleButton-popup'>
					<ToggleButton
						inactiveLabel={'off'}
	  				activeLabel={'on'}

					  value={ operational || false }
					  onToggle={(value) => {
					    toggleOperational(!value)
					  }} />
				</div>

				{(page !== "Main") && 
					<input 
						type='image' 
						className='backbutton' 
						src={Backarrow} 
						onClick={() => {
							setTitle("Termite");
							setPage("Main");
						}} >
					</input>
				}
			</div>

			<div className="PopupContents">

				{(page === "Main") && <MainPopup setPage={setPage} setTitle={setTitle}/> }

				{(page === "PolicyHygiene") && <PolicyHygienePopup setPage={setPage} setTitle={setTitle}/> }

				{(page === "Breakdown") && <BreakdownPopup setPage={setPage} setTitle={setTitle}/> }

				{(page === "Preferences") && <PreferencesPopup setPage={setPage} setTitle={setTitle}/> }

			</div>

			<div className="footer">
				<h1 id="footerh1">v 0.1.0.0</h1>
			</div>

		</div>
	)
}

export default Popup;