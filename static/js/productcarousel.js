document.addEventListener("DOMContentLoaded", function () {
    const slides = document.querySelectorAll(".carousel-slide");
    const indicators = document.querySelectorAll(".indicator");
    let currentSlide = 0;

    // Show the initial slide and highlight the indicator
    showSlide(currentSlide);

    // Function to display a specific slide
    function showSlide(index) {
        slides.forEach((slide) => {
            slide.style.display = "none";
        });
        slides[index].style.display = "block";

        indicators.forEach((indicator) => {
            indicator.classList.remove("active");
        });
        indicators[index].classList.add("active");
    }

    // Function to handle indicator click
    indicators.forEach((indicator, index) => {
        indicator.addEventListener("click", () => {
            currentSlide = index;
            showSlide(currentSlide);
        });
    });

    // Swipe functionality
    let touchStartX = null;

    document.addEventListener("touchstart", (e) => {
        touchStartX = e.touches[0].clientX;
    });

    document.addEventListener("touchend", (e) => {
        const touchEndX = e.changedTouches[0].clientX;
        const deltaX = touchStartX - touchEndX;

        if (deltaX > 30 && currentSlide < slides.length - 1) {
            currentSlide++;
        } else if (deltaX < -30 && currentSlide > 0) {
            currentSlide--;
        }

        showSlide(currentSlide);
    });
});
