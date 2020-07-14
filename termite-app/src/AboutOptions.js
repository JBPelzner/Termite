import React, {useState} from 'react';
import "./AboutOptions.css";

function AboutOptions() {
	return (
		<div className="AboutOptions">
			<div className="AboutOptions-Header">
				<h2 className="optionsh2">About Our Classifier</h2>
			</div>
			
					<h3 className="optionsh3">Mission</h3>

					<p className="AboutOptions-p"> Mission statement.</p>
					<h3 className="optionsh3">What goes into our models?</h3>
					
					<h4 className="optionsh4">Public Accessibility & Transparency</h4>
					<p className="AboutOptions-p"> Lets talk about public accessibility</p>

					<h4 className="optionsh4">Privacy Topics</h4>
					<p className="AboutOptions-p"> Lets talk about public accessibility</p>
					
					<h4 className="optionsh4">Recourse</h4>
					<p className="AboutOptions-p"> Did we give your site a bad grade by mistake? </p>
					
					<h3 className="optionsh3">How does our scoring work?</h3>
					<p className="AboutOptions-p">Anything except this text ugh.</p>
				
		</div>
	)
}

export default AboutOptions;