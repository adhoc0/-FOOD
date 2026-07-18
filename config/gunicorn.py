"""Gunicorn üretim başlangıç ayarları.

Bu modül Gunicorn zorunlu bağımlılığı eklemez; deployment komutu tarafından
okunabilecek güvenli varsayılanları dokümante eder.
"""

bind = "0.0.0.0:8000"
workers = 2
timeout = 60
accesslog = "-"
errorlog = "-"
