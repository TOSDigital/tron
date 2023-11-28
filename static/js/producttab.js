document.addEventListener("DOMContentLoaded", function () {
    const tabButtons = document.querySelectorAll(".tab-btn");
    const tabContents = document.querySelectorAll(".tab-content");

    tabButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const tabId = button.getAttribute("data-tab");

            tabButtons.forEach((btn) => {
                btn.classList.remove("active");
            });

            tabContents.forEach((content) => {
                content.style.display = "none";
            });

            button.classList.add("active");
            document.getElementById(tabId).style.display = "block";
        });
    });

    // Show the initial tab (e.g., "Description")
    tabButtons[0].click();
});
