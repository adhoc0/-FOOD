from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Kullanıcı oluşturma formu.

    Django'nun UserCreationForm'u varsayılan User modeline bağlıdır.
    Custom User Model kullandığımız için bu formu override etmeliyiz.
    Aksi halde admin panelinde kullanıcı oluşturma hata verir.
    """

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    """
    Kullanıcı düzenleme formu.

    Aynı sebepten ötürü UserChangeForm'u da override ediyoruz.
    İleride profil düzenleme sayfasında da bu form kullanılacak.
    """

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')
