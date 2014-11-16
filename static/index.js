$(window).load(function () {
    $("#temp").fadeIn(3000);
});

$(document).ready(function () {
	var ctx = document.getElementById("myChart").getContext("2d");

	var data = {
		labels: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
		datasets: [
			{
				label: "My First dataset",
				fillColor: "rgba(220,220,220,0.2)",
				strokeColor: "rgba(220,220,220,1)",
				pointColor: "rgba(220,220,220,1)",
				pointStrokeColor: "#fff",
				pointHighlightFill: "#fff",
				pointHighlightStroke: "rgba(220,220,220,1)",
				data: ['{{forcast_list[0]}}','{{forcast_list[1]}}','{{forcast_list[2]}}','{{forcast_list[3]}}',
				'{{forcast_list[4]}}', '{{forcast_list[5]}}','{{forcast_list[6]}}',]
			}]
		};
	var myLineChart = new Chart(ctx).Line(data);
});