import React, {useState, useEffect} from 'react';
import * as d3 from "d3";
import * as nv from "nvd3";
import "./UserReportsOptions.css";

function UserReportsOptions() {
	useEffect(() => {

		var scoreJSON = [{
			key: "Your Websites' Average Score Over Time",
			values: [{"x": 1,"y": 0.4}, {"x": 2,"y": 0.44}, {"x": 3,"y": 0.5}, {"x": 4,"y": 0.54}, {"x": 5,"y": 0.5}]}];

		var ratingJSON = [{
			key: "weeks",
			values: [{"label":"A","value":.45},{"label":"B","value":.13},{"label":"C","value":.05},{"label":"D","value":.14},{"label":"F","value":.23}]}];


		nv.addGraph(function () {
				var chart = nv.models.lineChart()
						.useInteractiveGuideline(true).margin({
							 top: 30,
							 right: 20,
							 bottom: 50,
							 left: 40
					 })
				;
				chart.xAxis
						.axisLabel('Week')
				;
				chart.yAxis
						.axisLabel('Score')
						.tickFormat(d3.format('.02f'))
				;
				d3.select('#scoreLineChart svg')
						.datum(scoreJSON)
						.call(chart)
				;
				nv.utils.windowResize(chart.update);
				return chart;
		});

		nv.addGraph(function () {
				var chart = nv.models.discreteBarChart()
				.x(function (d) {
								return d.label;
						})
						.y(function (d) {
								return d.value;
						})

				chart.xAxis
						.axisLabel('Score');

				chart.yAxis
						.tickFormat(d3.format('.02f'));

				d3.select('#distrBarChart svg')
						.datum(ratingJSON)
						.call(chart);

				nv.utils.windowResize(chart.update);

				return chart;
		});

		nv.addGraph(function () {
				var chart = nv.models.discreteBarChart().x(function (d) {
								return d.label;
						})
						.y(function (d) {
								return d.value;
						})

				chart.xAxis
						.axisLabel('Countries');

				chart.yAxis
						.tickFormat(d3.format('.02f'));

				d3.select('#distrBarChart2 svg')
						.datum(ratingJSON)
						.call(chart);

				nv.utils.windowResize(chart.update);

				return chart;
		});


	});

	return (
		<html lang="en">
		<head>
		  <meta charSet="utf-8"/>
		  <title>Making a Dashboard</title>
		  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/nvd3/1.8.6/nv.d3.css"></link>
		</head>
		<body>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.2/d3.min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/nvd3/1.8.6/nv.d3.js"></script>
		</body>


		<div className="UserReportsOptions">
			<div className="UserReportsOptions-Header">
				<h2 className="optionsh2">Internet Hygiene Reports</h2>
			</div>
			<div className="UserReportsOptions-Content">
			<div class="dashboard-flex-container">
			        <div
							id="scoreLineChart"
							class="with-3d-shadow with-transitions scoreLineChart">
			        <h2> Your Websites' Average Score by Week</h2>
							<svg>
							</svg>
			    </div>

			    <div
					id="distrBarChart"
					class="with-3d-shadow with-transitions distrBarChart">
			        <h2>Distribution of Your Websites' Scores</h2>
							<svg>
							</svg>
			    </div>

					<div
					id="distrBarChart2"
					class="with-3d-shadow with-transitions distrBarChart2">
			        <h2 className="optionsh2"> Global Distribution of Websites' Scores</h2>
							<svg>
							</svg>
			    </div>
			</div>
		</div>

		</div>


		{/* <script src= "./UserReportsHelper.js"> </script>;
		*/}
	</html>

)
};


export default UserReportsOptions;
