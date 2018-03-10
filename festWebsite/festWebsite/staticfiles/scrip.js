  var clock;

  $(document).ready(function() {

    // Grab the current date
    var currentDate = new Date();

    // Set some date in the future.
    var futureDate  = new Date("Apr 5, 2018 00:00:00")

    // Calculate the difference in seconds between the future and current date
    var diff = futureDate.getTime() / 1000 - currentDate.getTime() / 1000;

    // Instantiate a coutdown FlipClock
    clock = $('.time').FlipClock(diff, {
      clockFace: 'DailyCounter',
      countdown: true,
      showSeconds: true
    });
  });
  

