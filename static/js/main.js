(() => {
    const initializeSearchOverlay = () => {
        const searchToggle = document.querySelector("[data-search-toggle]");
        const searchOverlay = document.querySelector("[data-search-overlay]");

        if (!searchToggle || !searchOverlay) {
            return;
        }

        const searchInput = searchOverlay.querySelector("[data-search-input]");

        const setSearchOverlayState = (isOpen) => {
            searchOverlay.hidden = !isOpen;
            searchToggle.setAttribute("aria-expanded", String(isOpen));

            if (isOpen) {
                searchInput?.focus();
            }
        };

        searchToggle.addEventListener("click", (event) => {
            event.preventDefault();
            setSearchOverlayState(searchOverlay.hidden);
        });

        document.addEventListener("keydown", (event) => {
            if (event.key !== "Escape" || searchOverlay.hidden) {
                return;
            }

            setSearchOverlayState(false);
            searchToggle.focus();
        });
    };

    const initializeTabLists = () => {
        document.querySelectorAll("[data-tab-list]").forEach((tabList) => {
            const tabButtons = Array.from(
                tabList.querySelectorAll("[data-tab-target]"),
            );

            const activateTab = (selectedButton) => {
                tabButtons.forEach((tabButton) => {
                    const isSelected = tabButton === selectedButton;
                    const panelId = tabButton.dataset.tabTarget;
                    const panel = panelId
                        ? document.getElementById(panelId)
                        : null;

                    tabButton.classList.toggle("active", isSelected);
                    tabButton.setAttribute("aria-pressed", String(isSelected));

                    if (panel) {
                        panel.classList.toggle("active", isSelected);
                        panel.hidden = !isSelected;
                    }
                });
            };

            tabButtons.forEach((tabButton) => {
                tabButton.addEventListener("click", () => {
                    activateTab(tabButton);
                });
            });
        });
    };

    const initializePageInteractions = () => {
        initializeSearchOverlay();
        initializeTabLists();
    };

    if (document.readyState === "loading") {
        document.addEventListener(
            "DOMContentLoaded",
            initializePageInteractions,
            { once: true },
        );
    } else {
        initializePageInteractions();
    }
})();
