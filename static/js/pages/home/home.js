document.addEventListener('DOMContentLoaded', () => {
    const provinces = document.querySelectorAll('#svg-turkiye-haritasi g');
    const tooltip = document.getElementById('map-tooltip');
    const mapContainer = document.querySelector('.map-container');
    const modal = document.getElementById('kktc-modal');
    const modalCloseButton = document.querySelector('.modal-close');

    if (!tooltip || !mapContainer || provinces.length === 0) {
        return;
    }

    const provinceOffsets = {
        '34': { dx: -15, dy: -5 },   // İstanbul
        '17': { dx: 15, dy: 5 },     // Çanakkale
        '77': { dx: 0, dy: 5 },      // Yalova
        '41': { dx: 5, dy: 0 },      // Kocaeli
        '09': { dx: 10, dy: 0 },     // Aydın
        '45': { dx: 10, dy: 0 },     // Manisa
        '35': { dx: 5, dy: 0 },      // İzmir
        '48': { dx: 15, dy: 0 },     // Muğla
        '07': { dx: 5, dy: -5 },     // Antalya
        '33': { dx: 0, dy: 5 },      // Mersin
        '31': { dx: 5, dy: 5 }       // Hatay
    };

    provinces.forEach(province => {
        // Label ekleme mantığı
        const name = province.getAttribute('data-iladi');
        const plate = province.getAttribute('data-plakakodu');
        const isKibris = province.getAttribute('id') === 'kuzey-kibris';
        
        if (name && province.getAttribute('id') !== 'turkiye') {
            const bbox = province.getBBox(); // Grup sınırlarını da hesapla
            let centerX = bbox.x + bbox.width / 2;
            let centerY = bbox.y + bbox.height / 2;

            // Manuel offset düzeltmeleri
            if (plate && provinceOffsets[plate]) {
                centerX += provinceOffsets[plate].dx;
                centerY += provinceOffsets[plate].dy;
            }

            const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            text.setAttribute('x', centerX);
            text.setAttribute('y', centerY);
            text.setAttribute('text-anchor', 'middle');
            text.setAttribute('dominant-baseline', 'middle');
            text.setAttribute('class', 'province-label');
            text.style.pointerEvents = 'none';

            if (isKibris) {
                const tspanMain = document.createElementNS('http://www.w3.org/2000/svg', 'tspan');
                tspanMain.setAttribute('x', centerX);
                tspanMain.setAttribute('dy', '0');
                tspanMain.textContent = "KKTC";
                tspanMain.style.fontSize = '12px';
                tspanMain.style.fontWeight = 'bold';
                text.appendChild(tspanMain);
            } else if (plate) {
                const tspanPlate = document.createElementNS('http://www.w3.org/2000/svg', 'tspan');
                tspanPlate.setAttribute('x', centerX);
                tspanPlate.setAttribute('dy', '-0.3em'); // Plaka hafif yukarıda
                tspanPlate.textContent = plate;
                tspanPlate.style.fontSize = '12px';
                tspanPlate.style.fontWeight = '700';
                text.appendChild(tspanPlate);

                const tspanName = document.createElementNS('http://www.w3.org/2000/svg', 'tspan');
                tspanName.setAttribute('x', centerX);
                tspanName.setAttribute('dy', '1.2em'); // İsim plakanın altında
                tspanName.textContent = name;
                tspanName.style.fontSize = '9px';
                tspanName.style.fontWeight = '500';
                text.appendChild(tspanName);
            }

            province.appendChild(text);
        }

        // Etkileşimler
        province.addEventListener('mouseenter', () => {
            const name = province.getAttribute('data-iladi');
            if (name) {
                if (isKibris) {
                    tooltip.textContent = 'Kuzey Kıbrıs Türk Cumhuriyeti';
                } else {
                    tooltip.textContent = `${name} Mutfağı`;
                }
                tooltip.style.display = 'block';
                tooltip.style.opacity = '1';
            }
        });

        province.addEventListener('mousemove', (e) => {
            const containerRect = mapContainer.getBoundingClientRect();
            const x = e.clientX - containerRect.left;
            const y = e.clientY - containerRect.top;
            
            tooltip.style.left = `${x}px`;
            tooltip.style.top = `${y}px`;
        });

        province.addEventListener('mouseleave', () => {
            tooltip.style.opacity = '0';
            setTimeout(() => {
                tooltip.style.display = 'none';
            }, 200);
        });

        province.addEventListener('click', () => {
            const slug = province.getAttribute('id');
            const plate = province.getAttribute('data-plakakodu');
            const name = province.getAttribute('data-iladi');

            if (isKibris) {
                if (modal) {
                    modal.style.display = 'flex';
                }
            } else if (slug && slug !== 'turkiye') {
                // Remove active from all
                provinces.forEach(p => p.classList.remove('active'));
                // Add active to clicked
                province.classList.add('active');

                // Show selected action card
                const actionCard = document.getElementById('map-action-card');
                if (!actionCard) {
                    return;
                }

                const actionCardContent = document.createElement('span');
                const plateElement = document.createElement('strong');
                const nameElement = document.createElement('span');

                plateElement.textContent = plate || '';
                nameElement.textContent = name || '';
                actionCardContent.append(plateElement, nameElement);
                actionCard.replaceChildren(actionCardContent);

                if (actionCard instanceof HTMLAnchorElement) {
                    actionCard.href = `/il/${slug}/`;
                }
                actionCard.style.display = 'flex';
                
                // Small animation trick
                actionCard.style.animation = 'none';
                actionCard.offsetHeight; /* trigger reflow */
                actionCard.style.animation = 'slideUp 0.3s ease';
            }
        });
    });

    if (modal && modalCloseButton) {
        modalCloseButton.addEventListener('click', () => {
            modal.style.display = 'none';
        });
    }

    if (modal) {
        window.addEventListener('click', (event) => {
            if (event.target === modal) {
                modal.style.display = 'none';
            }
        });
    }
});
