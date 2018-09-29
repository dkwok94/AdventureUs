// Transitions the background image of the login page by fading in and out

// Webpage transition function
$(document).ready(function () {
  // Preload images
  let imgs = ['nathan-dumlao-576639-unsplash.jpg', 'jay-dantinne-499958-unsplash.jpg', 'john-towner-126926-unsplash.jpg', 'christopher-czermak-705859-unsplash.jpg', 'justin-lane-753659-unsplash.jpg'];
  let folder = "../../static/images/backgrounds/";
  imgs.forEach(function (img) {
    new Image().src = folder + img;
  });
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
