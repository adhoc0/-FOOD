export function isValidEmail(value) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(String(value).trim()); }
export function setFieldError(field, message) { const error = field.parentElement?.querySelector('[data-field-error]'); if (error) error.textContent = message; field.setAttribute('aria-invalid', message ? 'true' : 'false'); }
