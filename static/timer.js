$(document).ready(function(){
    var timer = new Timer();
	timer.start();
	timer.addEventListener('secondsUpdated', function (e) {
	    $('#basicUsage').html(timer.getTimeValues().toString());
	});			
});