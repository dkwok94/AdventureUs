// Delete trip button action
$(document).ready(function () {
  $('.delete').click(function () {
    $.ajax({
      type: 'DELETE',
      url: '/delete_trip/' + $('.delete').data('tripid'),
      success: function (url) {
	window.location.replace(url.redirect);
      }
    });
  });
});
