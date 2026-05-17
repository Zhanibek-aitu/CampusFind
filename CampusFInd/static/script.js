document.addEventListener("DOMContentLoaded", function () {
    setupThemeToggle();
    setupLiveSearch();
    setupDeleteConfirmations();
    setupCharacterCounter();
});


function setupThemeToggle() {
    const themeButton = document.getElementById("themeToggle");

    if (!themeButton) {
        return;
    }

    const savedTheme = localStorage.getItem("campusfind-theme");

    if (savedTheme === "dark") {
        document.body.classList.add("dark-mode");
        themeButton.textContent = "☀️ Light Mode";
    }

    themeButton.addEventListener("click", function () {
        document.body.classList.toggle("dark-mode");

        if (document.body.classList.contains("dark-mode")) {
            localStorage.setItem("campusfind-theme", "dark");
            themeButton.textContent = "☀️ Light Mode";
        } else {
            localStorage.setItem("campusfind-theme", "light");
            themeButton.textContent = "🌙 Dark Mode";
        }
    });
}


function setupLiveSearch() {
    const liveSearchInput = document.getElementById("liveSearch");
    const itemCards = document.querySelectorAll(".item-card");
    const visibleCount = document.getElementById("visibleCount");
    const noLiveResults = document.getElementById("noLiveResults");

    if (!liveSearchInput || itemCards.length === 0) {
        return;
    }

    liveSearchInput.addEventListener("input", function () {
        const searchText = liveSearchInput.value.toLowerCase().trim();
        let visibleItems = 0;

        itemCards.forEach(function (card) {
            const itemText = card.dataset.search.toLowerCase();

            if (itemText.includes(searchText)) {
                card.style.display = "block";
                visibleItems++;
            } else {
                card.style.display = "none";
            }
        });

        if (visibleCount) {
            visibleCount.textContent = visibleItems;
        }

        if (noLiveResults) {
            if (visibleItems === 0) {
                noLiveResults.style.display = "block";
            } else {
                noLiveResults.style.display = "none";
            }
        }
    });
}


function setupDeleteConfirmations() {
    const deleteForms = document.querySelectorAll(".delete-form");

    deleteForms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            const confirmed = confirm("Are you sure you want to delete this item?");

            if (!confirmed) {
                event.preventDefault();
            }
        });
    });
}


function setupCharacterCounter() {
    const descriptionInput = document.getElementById("description");
    const counter = document.getElementById("descriptionCounter");

    if (!descriptionInput || !counter) {
        return;
    }

    function updateCounter() {
        counter.textContent = descriptionInput.value.length + " characters";
    }

    descriptionInput.addEventListener("input", updateCounter);
    updateCounter();
}