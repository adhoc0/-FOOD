from django import forms
from .models import Recipe, Province

class RecipeCreateForm(forms.ModelForm):
    """
    Kullanıcıların yeni tarif göndermesi için form.
    """
    # Malzemeleri alt alta yazabilmesi için extra bir alan
    raw_ingredients = forms.CharField(
        label='Malzemeler',
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Her satıra bir malzeme yazın.\nÖrn:\n1 su bardağı un\n2 adet yumurta\nYarım çay kaşığı tuz'}),
        help_text='Her satıra bir malzeme ve miktarını yazın.'
    )
    
    class Meta:
        model = Recipe
        fields = [
            'province', 'title', 'description', 'instructions',
            'prep_time_minutes', 'cook_time_minutes', 'serving_size',
            'difficulty'
        ]
        widgets = {
            'province': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tarifin Adı'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Tarif hakkında kısa bir özet'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Adım adım yapılışı'}),
            'prep_time_minutes': forms.NumberInput(attrs={'class': 'form-control'}),
            'cook_time_minutes': forms.NumberInput(attrs={'class': 'form-control'}),
            'serving_size': forms.NumberInput(attrs={'class': 'form-control'}),
            'difficulty': forms.Select(attrs={'class': 'form-control'}),
        }
