/*******************************************************************************************/
// SERVICES DYNAMIC DISPLAY // 
/*******************************************************************************************/
// SERVICES DYNAMIC DISPLAY
const header = document.querySelector("#header");

// Add an event listener for the scroll event
window.addEventListener("scroll", () => {
    // Check if the page has been scrolled down by 100 pixels or more
    if (window.scrollY >= 100) {
        header.classList.add("height");
    } else {
        header.classList.remove("height");
    }
});

/*******************************************************************************************/
// ACTIVE NAVIGATION LINK TRACKING ON SCROLL // 
/*******************************************************************************************/
window.addEventListener('scroll', function() {
  var navButtons = document.querySelectorAll('.nav-btn');
  var sections = document.querySelectorAll('section');

  sections.forEach(function(section, index) {
    var rect = section.getBoundingClientRect();
    if ((rect.top <= window.innerHeight / 2) && (rect.bottom >= window.innerHeight / 2) || window.scrollY === 0) {
      navButtons.forEach(function(btn) {
        btn.classList.remove('active');
      });
      if (navButtons[index]) {
        navButtons[index].classList.add('active');
      }
    }
  });
  
  // Remove active class from all navigation buttons when scrolled back to the top
  if (window.scrollY === 0) {
    navButtons.forEach(function(btn) {
      btn.classList.remove('active');
    });
  }
});

  /*******************************************************************************************/
  // END OF ACTIVE NAVIGATION LINK TRACKING ON SCROLL // 
  /*******************************************************************************************/

/*******************************************************************************************/
// OWL CAROUSEL // 
/*******************************************************************************************/
$(document).ready(function(){
    $('.owl-carousel').owlCarousel({
        items:1,
        loop:true,
        nav:true,
        dots:true,
        autoplay:true,
        autoplaySpeed:3000,
        smartSpeed:1500,
        autoplayHoverPause:true
    });
});
/*******************************************************************************************/
// END OF OWL CAROUSEL // 
/*******************************************************************************************/