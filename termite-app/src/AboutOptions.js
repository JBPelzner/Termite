import React, {useState} from 'react';
import "./AboutOptions.css";

function AboutOptions() {
	return (
		<div className="AboutOptions">
			<div className="AboutOptions-Header">
				<h2 className="optionsh2">About Our Classifier</h2>
			</div>
			<div id="AboutOptions-Content">
			
					<h3 className="optionsh3">Our Mission</h3>

					<p className="AboutOptions-p"> Termite’s mission is to raise public education and awareness about matters related to online privacy. With a web scraper and NLP algorithms in the backend, we are able to analyze online privacy policies and user agreements in real-time, assigning scores to each respective policy according to our grading criteria. In the front end, the user is able to display visualizations of these policy scores for websites in their Google cache. The insights which our service provides empowers internet users to take control of their privacy and be more conscious about online data collection. 
</p>
					<h3 className="optionsh3">What goes into our model?</h3>
					
					<h4 className="optionsh4">Public Accessibility & Transparency</h4>
					<p className="AboutOptions-p"> We first and foremost rate privacy policies by how readable and approachable their policy documents are to the average user, and how transparent they are about their practices.</p>

					<h4 className="optionsh4">Privacy Topics</h4>
					<p className="AboutOptions-p"> Privacy values differ from person to person. Considering this, we break down privacy policies into six categories, and let the user decide what’s important to them. Here are the six categories: 
					<ol>
					<li>
					<u>Censorship and Suspension</u>: This category covers a web host’s stance on control and ownership of content, data, and services. It also covers deletion and suspension of accounts. Lastly, it covers how web hosts handle violations of community guidelines, as well as hate speech, libel and extremism. 
					</li>

					<li>
					<u>Deletion and Retention</u>: This category covers the user’s ability and rights to take action to delete their own data, cancel their accounts, as well as how long a web host keeps your data. Some web hosts exercise unlimited retention, while others limit their retention by deleting logs of your data on a regular basis, such as every 90 days. We also evaluate how vague or transparent a web host is with respect to its deletion and retention policies.
					</li>

					<li>
					<u>
					Cookie Policies and Other Forms of Tracking</u>: This covers how web hosts track you while using their services, for better or worse. Cookies are small pieces of data sent from a website and stored on the user's computer by the user's web browser while the user is browsing. Cookie policies govern activities such as tracking, collecting, storing, sharing, selling and otherwise optimizing a user’s experience, including targeted advertising. Seemingly delicious, cookies can be used to eat away at your privacy. Websites can also employ web beacons (also called page tags, pixels, pixel tags, and clear GIFs) to track user behavior, check that a user has accessed some content, and inform web analytics. A web beacon is a standardized set of protocols designed to allow web developers to track the activity of users without slowing down website response times. These tracking technologies are often used to customize your user experience, as well as to provide users with targeted advertising. It is worth noting that some people actually prefer to have targeted ads, if they’re going to have to see ads at all. Moreover, many wonderful features from web hosts would actually not be possible without tracking technologies. Further, there are some web hosts that cannot function at all without using some form of tracking technology.

					</li>

					<li>
					<u>Data Collection and Usage</u>: This covers what types of data web hosts collect, and for what use. Considering that the sensitivity of many data types collected is subjective, and that  it would be too difficult for an algorithm to understand the context of a privacy policy, we decided to evaluate policies on how transparent they are about the types of data they collect and for what purpose. 

					</li>

					<li>
					<u>Information Sharing and Selling</u>: This covers how and why web hosts may share or sell your data, if they do, for better or worse. Web hosts may share or sell your data for a variety of purposes, including advertising, medical or research purposes, legal compliance, analytics, government requests, criminal investigations, mergers, acquisitions, buyouts, and bankruptcy proceedings. These are all highly legitimate reasons. Whether these practices are morally good or bad is up for debate. We resolved this conundrum by asserting that not sharing information is ideal. In addition, there are levels to the way a web host shares your information. Websites can make the decision to only share anonymized and aggregated data. Others are transparent about sharing personally identifiable information (PII).
					</li>

					<li>
					<u>Policy Changes</u>: New features are always being made. Best practices, industry standards, and laws are constantly being crafted, molded, revised and updated. Companies can also just decide to change a policy on their own volition. All of this can require a web host to change their policies in part or in whole. We used 1) the mention and provision of policy archives, 2) date of last update, and 3) change notifications, as proxies to evaluate transparency. What if a web host updates its policy and discloses a questionable practice that it previously did not talk about? Although this may seem unsatisfactory, we felt that it shows a level of respectable transparency. In this category, we valued transparency over actual content. This is all to say that web hosts do need to update their privacy policies. Usually, these changes are in the best interest of users. That said, this covers how easy it is for user’s to gauge the history of a web host’s policies, and how forthcoming a web host is when it comes to notifying users about their changes.

					</li>

					</ol>
</p>
					
					<h3 className="optionsh3">How does our scoring work?</h3>
					<p className="AboutOptions-p">For each category, we created a rubric of practices we deemed were good or bad, and attributed points to those practices accordingly. We match the policy language against our scoring rubric, tally up the web host’s points, and generate a category score for the company. We then combine the individual category scores to generate a holistic score for the web host the user is using. With our personalized hygiene reports, we help the user visualize their overall online privacy behavior, as well as allowing them to view how they behave with respect to each privacy category.
</p>


					<h4 className="optionsh4">Recourse</h4>
					<p className="AboutOptions-p"> Did we give your site a bad grade by mistake? Please contact us at the link on the left, and we will get back to you to review your site's evaluation.</p>
					
					<h3 className="optionsh3">Special Thanks</h3>
					<p className="AboutOptions-p">We’d like to give a special thanks and “shouts outs” to Morgan Ames, Jared Maslin, and John Guerra for the clutch education. We could not have done this without your help and patience. Thank you also to Joyce Shen and David Steier for the opportunity and guidance they provided. We’d also like to thank Jacob Green, Eric Steckler, Raymond Stachowiak, and Nancy Hillestad. ♥ 
</p>

				</div>
		</div>
	)
}

export default AboutOptions;