/**
 * Lezzet Haritası — Ana JavaScript
 *
 * Yapı:
 * 1. DOM yüklendikten sonra çalışan event listener'lar
 * 2. Component başlatıcıları (init fonksiyonları)
 *
 * Neden jQuery veya başka kütüphane yok?
 * → Modern JavaScript (ES6+) ihtiyacımız olan her şeyi karşılıyor
 * → Gereksiz dependency = gereksiz yük + güvenlik yüzeyi
 * → Vanilla JS daha hızlı çalışır
 */

'use strict';

document.addEventListener('DOMContentLoaded', () => {
    initMobileMenu();
    initMessageDismiss();
});


/**
 * Mobil hamburger menü toggle
 *
 * Erişilebilirlik:
 * - aria-expanded durumu güncellenir
 * - Menü açıkken body scroll'u engellenir (opsiyonel)
 */
function initMobileMenu() {
    const toggle = document.getElementById('nav-toggle');
    const menu = document.getElementById('nav-menu');

    if (!toggle || !menu) return;

    toggle.addEventListener('click', () => {
        const isOpen = menu.classList.toggle('nav__menu--open');
        toggle.setAttribute('aria-expanded', isOpen);
    });

    // Menü dışına tıklayınca kapat
    document.addEventListener('click', (e) => {
        if (!toggle.contains(e.target) && !menu.contains(e.target)) {
            menu.classList.remove('nav__menu--open');
            toggle.setAttribute('aria-expanded', 'false');
        }
    });
}


/**
 * Flash mesajları kapatma butonu
 *
 * Event delegation kullanıyoruz:
 * → Her mesaja ayrı listener eklemek yerine document'a tek listener
 * → Dinamik olarak eklenen mesajlar da çalışır
 * → Daha az memory kullanımı
 */
function initMessageDismiss() {
    document.addEventListener('click', (e) => {
        const dismissBtn = e.target.closest('[data-dismiss="message"]');
        if (!dismissBtn) return;

        const message = dismissBtn.closest('[data-message]');
        if (!message) return;

        // Fade out animasyonu
        message.style.opacity = '0';
        message.style.transform = 'translateY(-10px)';
        message.style.transition = 'all 250ms ease';

        // Animasyon bitince DOM'dan kaldır
        setTimeout(() => message.remove(), 250);
    });
}
