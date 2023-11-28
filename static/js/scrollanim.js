document.addEventListener('DOMContentLoaded', () => {
  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      console.log(entry);
      if (entry.isIntersecting) {
        entry.target.classList.add('show');

        // Disconnect the observer once the element is visible
        observer.unobserve(entry.target);
      }
    });
  });

  const hiddenElements = document.querySelectorAll('.hidden');
  hiddenElements.forEach((el) => observer.observe(el));
});


