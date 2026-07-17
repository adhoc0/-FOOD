document.addEventListener('focusin', (event) => { const element = event.target.closest('[data-tooltip]'); if (element) element.setAttribute('title', element.dataset.tooltip); });
