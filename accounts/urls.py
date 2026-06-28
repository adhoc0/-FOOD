from django.urls import path
from django.contrib.auth import views as auth_views

from .views import RegisterView, CustomLoginView, ProfileView

app_name = 'accounts'

urlpatterns = [
    path('kayit/', RegisterView.as_view(), name='register'),
    path('giris/', CustomLoginView.as_view(), name='login'),
    path('cikis/', auth_views.LogoutView.as_view(), name='logout'),
    path('profil/', ProfileView.as_view(), name='profile'),
    
    # Password Reset URLs
    path('sifremi-unuttum/', 
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html', success_url='/hesap/sifre-sifirlama-gonderildi/'), 
         name='password_reset'),
         
    path('sifre-sifirlama-gonderildi/', 
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), 
         name='password_reset_done'),
         
    path('sifre-sifirla/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html', success_url='/hesap/sifre-sifirlama-tamamlandi/'), 
         name='password_reset_confirm'),
         
    path('sifre-sifirlama-tamamlandi/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), 
         name='password_reset_complete'),
]
