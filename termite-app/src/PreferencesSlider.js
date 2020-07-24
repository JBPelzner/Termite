import React, {useState} from 'react';
import './PreferencesSlider.css';


function PreferencesSlider(props) {

	return (
		<div className="PreferencesSlider">
		
    <div className="header">
  		<h3 class="lefth3">{props.title}</h3>	 
    </div>
		<div>
		<div class="PreferencesSlider-topicdesc">
			  	{props.description}
		</div>
  		
  		<input type="range" className='PreferencesSlider-input' min="1" max="7" onChange={(e) => props.setValue(parseInt(e.target.value))} value={props.value}/>
  		<label className='PreferencesSlider-label'>{props.value}</label>
  		
		</div>

		
		  

		</div>
	)
}

export default PreferencesSlider;