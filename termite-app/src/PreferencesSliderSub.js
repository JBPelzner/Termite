import React, {useState} from 'react';
import './PreferencesSliderSub.css';


function PreferencesSliderSub(props) {

	const [value, setValue] = useState(10);

	return (
		<div className="PreferencesSliderSub">
		
		<h4 className="lefth4">{props.title}</h4>	 
		<div>
  		<input type="range" className='PreferencesSliderSub-input' min="0" max="10" onChange={(e) => setValue(e.target.value)} value={value}/>
  		<label className="PreferencesSliderSub-label">{value}</label>
  		
		</div>

		
		  

		</div>
	)
}

export default PreferencesSliderSub;