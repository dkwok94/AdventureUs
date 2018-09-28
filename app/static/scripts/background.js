// Transitions the background image of the login page by fading in and out

$(document).ready(function () {
	let imgs = ['joshua-sortino-498896-unsplash.jpg', 'theodor-lundqvist-438530-unsplash.jpg', 'cristian-moscoso-1924-unsplash.jpg', 'nathan-dumlao-576639-unsplash.jpg', 'anthony-delanoix-575672-unsplash.jpg', 'karim-manjra-702188-unsplash.jpg', 'jay-dantinne-499958-unsplash.jpg', 'jeremy-bishop-346050-unsplash.jpg', 'robert-tudor-704838-unsplash.jpg', 'john-towner-126926-unsplash.jpg', 'bady-qb-751603-unsplash.jpg', 'caleb-miller-738108-unsplash.jpg', 'christopher-czermak-705859-unsplash.jpg', 'jonathan-gallegos-727409-unsplash.jpg', 'justin-lane-753659-unsplash.jpg', 'michael-liao-725983-unsplash.jpg', 'raphael-nogueira-559166-unsplash.jpg', 'robin-noguier-572033-unsplash.jpg', 'sorasak-252182-unsplash.jpg', 'usukhbayar-gankhuyag-726907-unsplash.jpg'];
  	$(function () {
      		let i = 0;
	  	setInterval(function () {
	      		i++;
		  	if (i == imgs.length) {
		      		i = 0;
		  	}
		      	$('body').css('background-image', 'url(../static/images/backgrounds/' + imgs[i] + ')');
	  	}, 5000);
  	});
});
