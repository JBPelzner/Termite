import React from 'react';
import './IconAndTextItem.css';


function IconAndTextItem(props) {
	return (
		<div className="IconAndTextItem">
		  
		  <div className='IconAndTextItem-icon' style={{backgroundColor:props.color}}></div>
			<div className='IconAndTextItem-text'> {props.text} </div>
			 
		  
		
		  

		</div>
	)
}

export default IconAndTextItem;