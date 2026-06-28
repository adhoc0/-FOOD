from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm
from interactions.models import Favorite, Comment


class RegisterView(CreateView):
    """
    Yeni kullanıcı kayıt görünümü.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/register.html'


class CustomLoginView(LoginView):
    """
    Giriş yapma görünümü.
    """
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class ProfileView(LoginRequiredMixin, TemplateView):
    """
    Kullanıcı profili görünümü.
    Sadece giriş yapmış kullanıcılar erişebilir.
    """
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Giriş yapan kullanıcının verilerini al
        user = self.request.user
        
        # Favoriye eklenen tarifler
        context['favorites'] = Favorite.objects.filter(user=user).select_related('recipe')
        
        # Kullanıcının yaptığı yorumlar
        context['comments'] = Comment.objects.filter(user=user).select_related('recipe')
        
        return context
