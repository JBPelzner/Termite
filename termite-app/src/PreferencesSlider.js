import React, {useState} from 'react';
import './PreferencesSlider.css';


function PreferencesSlider(props) {

	const [value, setValue] = useState(7);

	return (
		<div className="PreferencesSlider">
		
    <div className="header">
  		<h3 class="lefth3">{props.title}</h3>	 
    </div>
		<div>
		<div class="PreferencesSlider-topicdesc">
			  	{props.description}
		</div>
  		
  		<input type="range" className='PreferencesSlider-input' min="1" max="7" onChange={(e) => setValue(e.target.value)} value={value}/>
  		<label className='PreferencesSlider-label'>{value}</label>
  		
		</div>

		
		  

		</div>
	)
}

export default PreferencesSlider;