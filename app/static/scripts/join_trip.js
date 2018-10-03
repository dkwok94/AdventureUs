// Event handler for 'JOIN TRIP' button press

$(document).ready(function () {
  $('.join').click(function () {
    console.log("Pressed");
    $.ajax({
      type: 'POST',
      url: '/send_notification/' + $('.join').attr('data-tripid'),
      contentType: 'application/json',
      data: {},
      success: function (response) {
	alert(response.response);
	$('#tripInfo').modal('hide');
      },
      error: function (error) {
	alert(error);
      }
    });
  });
});
