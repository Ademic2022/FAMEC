/*******************************************************************************************/
// DYNAMIC DISPLAY // 
/*******************************************************************************************/
const header = document.querySelector("#header");
const sections = document.querySelectorAll('section');
const featureDropdown = document.querySelector('#featureDropdown');
const solutionDropdown = document.querySelector('#solutionDropdown');

// Add an event listener for the scroll event
/*******************************************************************************************/
// ACTIVE NAVIGATION LINK TRACKING ON SCROLL // 
/*******************************************************************************************/
window.addEventListener('scroll', function() {
  var navButtons = document.querySelectorAll('.nav-btn');
  // var sections = document.querySelectorAll('section');
  // Check if the page has been scrolled down by 100 pixels or more
  if (window.scrollY >= 100) {
      header.classList.add("height");
  } else {
      header.classList.remove("height");
  }
  sections.forEach((event)=>{
    let top = window.scrollY;
    let offset = event.offsetTop - 150;
    let height = event.offsetHeight;

    if (top >= offset && top < offset + height){
      event.classList.add('show-animate')
    }
    else {
      event.classList.remove('show-animate')
    }
  });
});

/*******************************************************************************************/
// END OF ACTIVE NAVIGATION LINK TRACKING ON SCROLL // 
/*******************************************************************************************/

/*******************************************************************************************/
// PAGE SMOOTH SCROLL // 
/*******************************************************************************************/
var navLinks = document.querySelectorAll('a.nav-btn');
var navbarHeight = 100;

navLinks.forEach((link) => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    var target = document.querySelector(link.getAttribute('href'));
    
    if (target.getAttribute('id' === 'home')) {
      // Scroll to the top of the page, leaving space for the navbar
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
      // Scroll to the target, accounting for the navbar height
      var scrollPosition = target.offsetTop - navbarHeight;
      window.scrollTo({ top: scrollPosition, behavior: 'smooth' });
    }
  });
});


/*******************************************************************************************/
// END OF PAGE SMOOTH SCROLL // 
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
/*******************************************************************************************/
// Feature Navigation Dropdown // 
/*******************************************************************************************/
const features = document.querySelectorAll('#dropdown');
features.forEach((event)=>{
  event.addEventListener('click', ()=>{
    
    if (event.classList.contains('features')) {
      featureDropdown.classList.toggle('showDropdown');
    } else {
      solutionDropdown.classList.toggle('showDropdown');
    }
    
    // Toggle the chevron icon
    const bx = event.querySelector('.bx');
    if (bx.classList.contains('bx-chevron-down')) {
      bx.classList.toggle('bx-chevron-up');
    }

    // Close the other dropdown if it's open
    if (event.classList.contains('features') && solutionDropdown.classList.contains('showDropdown')) {
      solutionDropdown.classList.remove('showDropdown');
      const solutionBx = document.querySelector('.solution .bx');
      solutionBx.classList.remove('bx-chevron-up');
    } else if (!event.classList.contains('features') && featureDropdown.classList.contains('showDropdown')) {
      featureDropdown.classList.remove('showDropdown');
      const featureBx = document.querySelector('.features .bx');
      featureBx.classList.remove('bx-chevron-up');
    }
    // mobile functionality for Back icon
    const backBtn = document.querySelectorAll('.menu-icon-back')
    backBtn.forEach((e)=>{
      e.addEventListener('click', ()=>{
        if (featureDropdown.classList.contains('showDropdown')) {
          featureDropdown.classList.remove('showDropdown');
        }
        else if (solutionDropdown.classList.contains('showDropdown')) {
          solutionDropdown.classList.remove('showDropdown');
        }
      })
    })
  })
})


const closeBtn = document.querySelectorAll('.menu-icon-close')
const closeCheckbox = document.getElementById("check");
const navigation = document.querySelector(".navigation");
closeCheckbox.addEventListener('click', ()=>{
  if (closeCheckbox.checked == true){
    navigation.style.height = '100vh'
    closeBtn.forEach((e)=>{
      e.addEventListener('click', ()=>{
        if (featureDropdown.classList.contains('showDropdown')){
          featureDropdown.classList.remove('showDropdown');
        }
        else{
          solutionDropdown.classList.remove('showDropdown');
        }
        closeCheckbox.checked = false
        navigation.style.height = 0
      })
    })
  }
  else{
    navigation.style.height = 0
  }
})
