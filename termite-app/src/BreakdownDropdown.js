import React, {useState} from 'react';
import './BreakdownDropdown.css';
import IconAndTextItem from './IconAndTextItem.js';
import SidewaysDropArrow from './dropdownarrow-sideways.png';
import DropArrow from './dropdownarrow.png';


function BreakdownDropdown(props) {

const [dropped, setDropped] = useState(false);


	return (
		<div className="BreakdownDropdown">


			
			<div className="BreakdownDropdown-DropRow">

				<button className="BreakdownDropdown-Button" onClick={() => setDropped(!dropped)} >
					<div className="BreakdownDropdown-TopicItem">
				 		<IconAndTextItem color={props.color} text={props.text} />
				 	</div>
				 	<img className="BreakdownDropdown-Arrow" src={dropped ? DropArrow : SidewaysDropArrow} />


				</button>
				
				{(dropped === true) &&  
					<p className="BreakdownDropdown-Description">
						{props.description}
					</p>
				}

			 </div>

		  
		

		  

		</div>
	)
}

export default BreakdownDropdown;