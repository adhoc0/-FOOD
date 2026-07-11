from django import forms

from recipes.models import Recipe


class RecipeCreateForm(forms.ModelForm):
    """Recipe creation form."""

    raw_ingredients = forms.CharField(
        label="Malzemeler",
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 6,
                "placeholder": (
                    "Her satıra bir malzeme yazın.\n"
                    "Örnek:\n"
                    "500 g Un\n"
                    "2 Adet Yumurta\n"
                    "1 Tatlı Kaşığı Tuz"
                ),
            }
        ),
        help_text="Her satıra bir malzeme yazın.",
    )

    class Meta:
        model = Recipe

        fields = [
            "province",
            "category",
            "title",
            "summary",
            "instructions",
            "preparation_time",
            "cooking_time",
            "servings",
            "difficulty",
        ]

        widgets = {
            "province": forms.Select(
                attrs={"class": "form-control"},
            ),
            "category": forms.Select(
                attrs={"class": "form-control"},
            ),
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Tarif Başlığı",
                },
            ),
            "summary": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Tarif hakkında kısa açıklama",
                },
            ),
            "instructions": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 8,
                    "placeholder": "Tarifin hazırlanışını adım adım yazın.",
                },
            ),
            "preparation_time": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 0,
                },
            ),
            "cooking_time": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 0,
                },
            ),
            "servings": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                },
            ),
            "difficulty": forms.Select(
                attrs={
                    "class": "form-control",
                },
            ),
        }