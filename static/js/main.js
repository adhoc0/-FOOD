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

    // Favori / yorum / puan formları: JS varsa sayfa yenilenmeden gönderilir,
    // yoksa (veya beklenmeyen bir yanıtta) normal form gönderimi çalışır.
    const initializeAjaxForms = () => {
        const status = document.querySelector("[data-interaction-status]");

        const showMessages = (items) => {
            if (!status) {
                return;
            }

            status.replaceChildren(
                ...items.map(({ level, text }) => {
                    const element = document.createElement("p");
                    element.className = `message message-${level}`;
                    element.textContent = text;
                    return element;
                }),
            );
        };

        const applyResult = (kind, form, data) => {
            if (kind === "favorite" && typeof data.favorited === "boolean") {
                const button = form.querySelector("[data-favorite-button]");

                if (button) {
                    button.setAttribute("aria-pressed", String(data.favorited));
                    button.textContent = data.favorited
                        ? "Favorilerimden çıkar"
                        : "Favorilerime ekle";
                }
            }

            if (kind === "comment") {
                const summary = document.querySelector("[data-rating-summary]");

                if (summary && data.average_rating !== undefined) {
                    summary.textContent = `★ ${data.average_rating} (${data.rating_count})`;
                }

                if (data.ok) {
                    form.reset();
                }
            }
        };

        document.querySelectorAll("[data-ajax-form]").forEach((form) => {
            form.addEventListener("submit", async (event) => {
                event.preventDefault();

                const submitButton = form.querySelector("[type=submit]");
                submitButton?.setAttribute("disabled", "");
                form.setAttribute("aria-busy", "true");

                try {
                    const response = await fetch(form.action, {
                        method: "POST",
                        body: new FormData(form),
                        headers: { Accept: "application/json" },
                        credentials: "same-origin",
                    });
                    const isJson = (response.headers.get("Content-Type") || "")
                        .includes("application/json");

                    if (!isJson) {
                        // Oturum düşmüş (giriş sayfasına yönlendirme) vb.: normal akış.
                        form.submit();
                        return;
                    }

                    const data = await response.json();
                    showMessages(data.messages || []);
                    applyResult(form.dataset.ajaxForm, form, data);
                } catch {
                    form.submit();
                } finally {
                    submitButton?.removeAttribute("disabled");
                    form.removeAttribute("aria-busy");
                }
            });
        });
    };

    const initializePageInteractions = () => {
        initializeSearchOverlay();
        initializeTabLists();
        initializeAjaxForms();
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
