document.documentElement.classList.add('js');
document.addEventListener('keydown', (event) => { if (event.key === 'Escape') document.querySelectorAll('[role="dialog"]:not([hidden])').forEach((dialog) => dialog.setAttribute('hidden', '')); });
