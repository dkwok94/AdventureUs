// Notification page dynamic button modal loading
// Sent request modal loading
$(document).ready(function () {
  $('.sentnote').click(function () {
    $.ajax({
      type: 'GET',
      url: '/get_trip/' + $(this).data('tripid'),
      contentType: 'application/json',
      success: function (trip) {
	console.log(trip);
	$('.sent-modal-body').empty();
	$('.sent-modal-body').append('<DIV class="inforow"><DIV class="tripcolumn"><H5 class="notemodaltext">' + trip.city + ', ' + trip.country + ' ' + '(' + trip.date_range + ')' + '</H5><H6 class="notemodaltext">Request to ' + trip.host + ' pending!</H6></DIV></DIV>');
      },
      error: function (error) {
	$('.sent-modal-body').append('<DIV class="inforow"><DIV class="tripcolumn"><H5 class="notemodaltext">Trip is not in the database</H5></DIV></DIV>');
      }
    });
  });
});

// Received request modal loading
$(document).ready(function () {
  $('.receivenote').click(function () {
    button_pressed = $(this)
    $.ajax({
      type: 'GET',
      url: '/get_trip/' + button_pressed.data('tripid'),
      contentType: 'application/json',
      success: function (trip) {
	console.log(trip);
	$('.receive-modal-body').empty();
	$('.receive-modal-body').append('<DIV class="inforow"><DIV id="receive-column" class="tripcolumn"><H5 class="notemodaltext">' + trip.city + ', ' + trip.country + ' ' + '(' + trip.date_range + ')' + '</H5></DIV></DIV>');
	$('#received_notification_dialog').attr('data-tripid', trip.id);
	$('#received_notification_dialog').attr('data-noteid', button_pressed.data('id'));
	  $.ajax({
	    type: 'GET',
	    url: '/get_sender/' + button_pressed.data('id'),
	    contentType: 'application/json',
	    success: function (sender) {
	      console.log(sender);
	      $('#receive-column').append('<H6 class="notemodaltext">' + sender.first_name + ' ' + sender.last_name + ' (' + sender.username + ')' + ' has requested to join!</H6><IMG src="' + sender.profile_pic + '" class="img-circle img-responsive note-person">');
	    },
	    error: function(response) {
	      $('#receive-column').append('<H6 class="notemodaltext">Sender does not exist</H6>');
	    }
	  });
      },
      error: function (error) {
	$('.receive-modal-body').append('<DIV class="inforow"><DIV class="tripcolumn"><H5 class="notemodaltext">Trip is not in the database</H5></DIV></DIV>');
      }
    });
  });
});

// Accept button action for the received notification modal
$(document).ready(function () {
  $('.accept').click(function () {
    $.ajax({
      type: 'GET',
      url: '/notification/' + $('#received_notification_dialog').data('noteid') + '/accepted_request/' + $('#received_notification_dialog').data('tripid'),
      success: function (url) {
	window.location.replace(url.redirect);
      }
    });
  });
});
