document.addEventListener('DOMContentLoaded', async () => {
    const root = document.querySelector('[data-map-root]');
    const mapHost = root?.querySelector('[data-map-src]');
    if (!root || !mapHost) return;

    try {
        const response = await fetch(mapHost.dataset.mapSrc, { credentials: 'same-origin' });
        if (!response.ok) throw new Error('Harita yüklenemedi');
        mapHost.innerHTML = await response.text();
        const svg = mapHost.querySelector('svg');
        if (!svg) throw new Error('Geçersiz harita SVG');
        // Eski SVG dosyasında viewBox yok; görünür Türkiye siluetini ölçüp
        // kapsayıcıya ortalayarak boşluk ve sağ-üst kaymasını kaldırıyoruz.
        const bounds = svg.getBBox();
        const padding = Math.max(bounds.width, bounds.height) * 0.035;
        svg.setAttribute('viewBox', `${bounds.x - padding} ${bounds.y - padding} ${bounds.width + padding * 2} ${bounds.height + padding * 2}`);
        svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
        svg.removeAttribute('width');
        svg.removeAttribute('height');

        const provinces = [...svg.querySelectorAll('[id^="TR-"]')];
        const tooltip = root.querySelector('[data-map-tooltip]');
        const action = root.querySelector('[data-map-action]');
        const code = root.querySelector('[data-map-code]');
        const name = root.querySelector('[data-map-name]');
        const activeProvince = root.dataset.activeProvince;

        provinces.forEach((province) => {
            const plate = province.id.replace('TR-', '').replace(/^0+/, '').padStart(2, '0');
            province.setAttribute('tabindex', '0');
            province.setAttribute('role', 'button');
            province.setAttribute('aria-label', `İl ${plate}`);

            const showHover = (event) => {
                province.classList.add('is-hover');
                if (!tooltip) return;
                tooltip.textContent = `İl ${plate}`;
                tooltip.classList.add('is-visible');
                const bounds = root.querySelector('.turkey-map').getBoundingClientRect();
                tooltip.style.left = `${event.clientX - bounds.left}px`;
                tooltip.style.top = `${event.clientY - bounds.top}px`;
            };
            const hideHover = () => { province.classList.remove('is-hover'); tooltip?.classList.remove('is-visible'); };
            const selectProvince = () => {
                provinces.forEach((item) => item.classList.remove('is-selected'));
                province.classList.add('is-selected');
                if (code) code.textContent = plate;
                if (name) name.textContent = `İl ${plate} tariflerini gör`;
                if (action) { action.hidden = false; action.href = action.dataset.provinceListUrl || '/provinces/'; }
            };

            province.addEventListener('pointerenter', showHover);
            province.addEventListener('pointermove', showHover);
            province.addEventListener('pointerleave', hideHover);
            province.addEventListener('focus', () => province.classList.add('is-hover'));
            province.addEventListener('blur', hideHover);
            province.addEventListener('click', selectProvince);
            province.addEventListener('keydown', (event) => {
                if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); selectProvince(); }
            });
            if (activeProvince && province.id.toLowerCase().includes(activeProvince.toLowerCase())) province.classList.add('is-active');
        });
    } catch (error) {
        mapHost.setAttribute('role', 'img');
        mapHost.setAttribute('aria-label', 'Türkiye iller haritası');
        console.error(error);
    }
});
