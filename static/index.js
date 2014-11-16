$(window).load(function () {
    $("#temp").fadeIn(3000);
});

function week_forecast_chart(tempData){
	var ctx = document.getElementById("weekForecast").getContext("2d");
	
	var d = new Date();
	var weekday = new Array(7);
		weekday[0] = "Sunday";
		weekday[1] = "Monday";
		weekday[2] = "Tuesday";
		weekday[3] = "Wednesday";
		weekday[4] = "Thursday";
		weekday[5] = "Friday";
		weekday[6] = "Saturday";
	var t = d.getDay();

	var data = {
		labels: [
			weekday[t], 
			weekday[(t+1)%7], 
			weekday[(t+2)%7], 
			weekday[(t+3)%7], 
			weekday[(t+4)%7], 
			weekday[(t+5)%7], 
			weekday[(t+6)%7]
		],
		datasets: [
			{
				label: "My First dataset",
				fillColor: "rgba(220,220,220,0.2)",
				strokeColor: "rgba(220,220,220,1)",
				pointColor: "rgba(220,220,220,1)",
				pointStrokeColor: "#fff",
				pointHighlightFill: "#fff",
				pointHighlightStroke: "rgba(220,220,220,1)",
				data: tempData
			}]
		};
	var myLineChart = new Chart(ctx).Line(data);
}