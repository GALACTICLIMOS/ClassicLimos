let currentIndex = 0;
const slides = document.querySelectorAll('.slide');
const sliderWrapper = document.querySelector('.slider-wrapper');
const slideInterval = 2000; // Change slide every 2 seconds (2000 milliseconds)

function showSlide(index) {
    if (index < 0) {
        currentIndex = slides.length - 1;
    } else if (index >= slides.length) {
        currentIndex = 0;
    }

    const offset = -currentIndex * 100; // 100% is the width of each slide
    sliderWrapper.style.transform = `translateX(${offset}%)`;
}

function prevSlide() {
    currentIndex--;
    showSlide(currentIndex);
}

function nextSlide() {
    currentIndex++;
    showSlide(currentIndex);
}

// Auto-advancement of slides
setInterval(() => {
    currentIndex++;
    showSlide(currentIndex);
}, slideInterval);

showSlide(currentIndex);
