// Get DOM elements
const header = document.querySelector("#header");
const sections = document.querySelectorAll('section');
const featureDropdown = document.querySelector('#featureDropdown');
const solutionDropdown = document.querySelector('#solutionDropdown');
const navLinks = document.querySelectorAll('a.nav-btn');
const closeCheckbox = document.getElementById("check");
const navigation = document.querySelector(".navigation");

// Add scroll event listener
window.addEventListener('scroll', () => {
  const navButtons = document.querySelectorAll('.nav-btn');

  if (window.scrollY >= 100) {
    header.classList.add("height");
  } else {
    header.classList.remove("height");
  }

  sections.forEach((section) => {
    let top = window.scrollY;
    let offset = section.offsetTop - 150;
    let height = section.offsetHeight;

    if (top >= offset && top < offset + height) {
      section.classList.add('show-animate');
    } else {
      section.classList.remove('show-animate');
    }
  });
});

// Add click event listener to navigation links for smooth scrolling
navLinks.forEach((link) => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const target = document.querySelector(link.getAttribute('href'));

    if (target.getAttribute('id' === 'home')) {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
      const scrollPosition = target.offsetTop - 100; // Adjusted for navbar height
      window.scrollTo({ top: scrollPosition, behavior: 'smooth' });
    }
  });
});

// Initialize Owl Carousel
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

// Feature Navigation Dropdown
const features = document.querySelectorAll('#dropdown');
features.forEach((event) => {
  event.addEventListener('click', () => {
    if (event.classList.contains('features')) {
      featureDropdown.classList.toggle('showDropdown');
    } else {
      solutionDropdown.classList.toggle('showDropdown');
    }

    const bx = event.querySelector('.bx');
    bx.classList.toggle('bx-chevron-up');

    if (event.classList.contains('features') && solutionDropdown.classList.contains('showDropdown')) {
      solutionDropdown.classList.remove('showDropdown');
      document.querySelector('.solution .bx').classList.remove('bx-chevron-up');
    } else if (!event.classList.contains('features') && featureDropdown.classList.contains('showDropdown')) {
      featureDropdown.classList.remove('showDropdown');
      document.querySelector('.features .bx').classList.remove('bx-chevron-up');
    }
  });
});

// Add click event listeners to close buttons
const closeBtn = document.querySelectorAll('.menu-icon-close');
closeBtn.forEach((btn) => {
  btn.addEventListener('click', () => {
    if (featureDropdown.classList.contains('showDropdown')) {
      featureDropdown.classList.remove('showDropdown');
    } else {
      solutionDropdown.classList.remove('showDropdown');
    }
    closeCheckbox.checked = false;
    navigation.style.height = 0;
  });
});

// Add click event listener to close checkbox
closeCheckbox.addEventListener('click', () => {
  if (closeCheckbox.checked) {
    navigation.style.height = '100vh';
  } else {
    navigation.style.height = 0;
  }
});
