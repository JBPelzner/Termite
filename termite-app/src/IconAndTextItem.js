import React from 'react';
import './IconAndTextItem.css';


function IconAndTextItem(props) {
	return (
		<div className="IconAndTextItem">
		  
		  
			<div className='IconAndTextItem-text'> 
				{props.text}
			 </div>

			<div className='IconAndTextItem-scorebox' 
				style=
					{{backgroundColor:props.color, 
						borderColor:props.color
					}}
				>
					{props.score}
				</div>
			 
		  
		
		  

		</div>
	)
}

export default IconAndTextItem;