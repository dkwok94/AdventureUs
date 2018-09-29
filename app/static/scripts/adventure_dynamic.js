// Dynamic Modal Content Loading Function for Adventures Page

$(document).ready(function () {
  $('.activetrip').click(function () {
    let id = $(this).data('id');
    let data = {"id": id};
    let json = JSON.stringify(data);
    $('.trip-header').empty();
    $('.trip-body').empty();
    $('.trip-footer>.buddies').empty();

   // Dynamic AJAX request for trip based on trip ID of button
    $.ajax({
      type: 'POST',
      url: '/adventures',
      contentType: 'application/json',
      data: json,
      success: function (trip) {
        console.log(trip.users);
	$('.trip-header').append('<H2 class="modal-title" id="where">' + trip.city + ', ' + trip.country + '</H2><BUTTON type="button" class="close" data-dismiss="modal" aria-label="Close">&times;</BUTTON>');
	$('.trip-body').append('<DIV class="inforow"><DIV class="tripcolumn"><H4 class="host tripmodaltext"><STRONG>HOST</STRONG><H4><H5 class="hostname tripmodaltext">' + trip.host_firstname + ' ' + trip.host_lastname + '</H5><H6 class="hostname tripmodaltext">' + trip.host + '</H6><IMG src="' + trip.host_pic + '" class="img-circle img-responsive person" alt="' + trip.host_firstname + '"></DIV><DIV class="tripcolumn"><H4 class="tripinformation tripmodaltext"><STRONG>TRIP INFORMATION</STRONG></H4><H4 class="daterange tripmodaltext">' + trip.date_range + '</H4><P class="tripdescription tripmodaltext">' + trip.description + '</P></DIV></DIV>');
	$.ajax({
	  type: 'POST',
	  url: '/trip_roster',
	  contentType: 'application/json',
	  data: JSON.stringify({"users": trip.users}),
	  success: function (users) {
 	    $('.trip-footer>.buddies').append('<P class="others modalfootertext">Other users on this trip:</P><DIV class="buddiesrow"></DIV>');
	    for (user of users) {
	      $('.trip-footer>.buddies>.buddiesrow').append('<IMG src="' + user.profile_pic + '" class="img-circle rowperson" alt="' + user.first_name + '">');
	    }
	    $('.trip-footer').append('</DIV>');	    
	  },
	  error: function (response) {
	    $('.trip-footer').append('<P class="others modalfootertext">No users are currently on this trip</P>');
	  }
	 });
      },
      error: function (response) {
        $('.trip-header').append('<H2 class="modal-title" id="where">Trip Not Found</H2>');
      }
    });
  });
});

// Dynamic Modal Content Loader for Profile Page

$(document).ready(function () {
  $('.profileactivetrip').click(function () {
    let id = $(this).data('id');
    let data = {"id": id};
    let json = JSON.stringify(data);
    $('.trip-header').empty();
    $('.trip-body').empty();
    $('.trip-footer>.buddies').empty();

   // Dynamic AJAX request for trip based on trip ID of button
    $.ajax({
      type: 'POST',
      url: '/adventures',
      contentType: 'application/json',
      data: json,
      success: function (trip) {
        console.log(trip.users);
	$('.trip-header').append('<H2 class="modal-title" id="where">' + trip.city + ', ' + trip.country + '</H2><BUTTON type="button" class="close" data-dismiss="modal" aria-label="Close">&times;</BUTTON>');
	$('.trip-body').append('<DIV class="inforow"><DIV class="tripcolumn"><H4 class="host tripmodaltext"><STRONG>HOST</STRONG><H4><H5 class="hostname tripmodaltext">' + trip.host_firstname + ' ' + trip.host_lastname + '</H5><H6 class="hostname tripmodaltext">' + trip.host + '</H6><IMG src="' + trip.host_pic + '" class="img-circle img-responsive person" alt="' + trip.host_firstname + '"></DIV><DIV class="tripcolumn"><H4 class="tripinformation tripmodaltext"><STRONG>TRIP INFORMATION</STRONG></H4><H4 class="daterange tripmodaltext">' + trip.date_range + '</H4><P class="tripdescription tripmodaltext">' + trip.description + '</P></DIV></DIV>');
	$.ajax({
	  type: 'POST',
	  url: '/trip_roster',
	  contentType: 'application/json',
	  data: JSON.stringify({"users": trip.users}),
	  success: function (users) {
 	    $('.trip-footer>.buddies').append('<P class="others modalfootertext">Other users on this trip:</P><DIV class="buddiesrow"></DIV>');
	    for (user of users) {
	      $('.trip-footer>.buddies>.buddiesrow').append('<IMG src="' + user.profile_pic + '" class="img-circle rowperson" alt="' + user.first_name + '">');
	    }
	    $('.trip-footer').append('</DIV>');	    
	  },
	  error: function (response) {
	    $('.trip-footer').append('<P class="others modalfootertext">No users are currently on this trip</P>');
	  }
	 });
      },
      error: function (response) {
        $('.trip-header').append('<H2 class="modal-title" id="where">Trip Not Found</H2>');
      }
    });
  });
});
