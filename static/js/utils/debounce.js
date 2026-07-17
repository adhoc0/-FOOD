export function debounce(callback, wait = 250) { let timeout; return (...args) => { window.clearTimeout(timeout); timeout = window.setTimeout(() => callback(...args), wait); }; }
