# Sonraki çalışma oturumu

## Başlangıç durumu

- Yeni yemek platformu kurumsal paleti uygulandı.
- Renklerin tek kaynağı `static/css/base/variables.css`.
- Harita SVG olarak etkileşimli hale getirildi.
- Harita durumları: normal, hover, seçili ve aktif il.
- Göller için yalnızca `--color-lake` mavi token'ı kullanılıyor.
- Son gönderilen commit: `c0ea0a4`.

## Uygulama sırası

1. Haritayı gerçek tarayıcıda görsel olarak kontrol et.
2. Normal, hover, seçili ve aktif il durumlarını tek tek doğrula.
3. Göl rengini ve il sınırlarını tüm ekranlarda kontrol et.
4. Mobil ve tablet responsive kontrolü yap.
5. Ana sayfa, tarif listeleme ve tarif detayında renk tutarlılığını test et.
6. Eski CSS dosyalarındaki sabit renkleri temizle; renkleri `variables.css` token'larına bağla.
7. JavaScript etkileşimlerini ve erişilebilirlik kontrollerini tamamla.
8. Tam performans, güvenlik ve test paketini çalıştır.
9. Docker staging smoke test yap.
10. Son aşamada production domain ve mail yapılandırmasına geç.

## Kontrol komutları

```powershell
$env:DJANGO_SETTINGS_MODULE='core.test_settings'
.\.venv\Scripts\python.exe manage.py check --settings=core.test_settings
.\.venv\Scripts\python.exe -m pytest -q
```
