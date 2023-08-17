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
      if ((rect.top <= 1 && rect.top <= window.innerHeight) || window.scrollY === 0) {
        navButtons.forEach(function(btn) {
          btn.classList.remove('active');
        });
        if (navButtons[index]) {
          navButtons[index].classList.add('active');
        }
      }
    });
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
        autoplaySpeed:1000,
        smartSpeed:1500,
        autoplayHoverPause:false
    });
});
/*******************************************************************************************/
// END OF OWL CAROUSEL // 
/*******************************************************************************************/