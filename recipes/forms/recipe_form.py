from django import forms
from django.core.exceptions import ValidationError

from recipes.models import Recipe
from recipes.validators import RecipeValidator


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

    def clean(self):
        """Tüm form verilerini doğrula."""
        cleaned_data = super().clean() or {}

        try:
            RecipeValidator.validate_recipe_data(cleaned_data)
        except ValidationError as e:
            # Validator bir dict içinde hatalar döndürebilir, bunları forma ekliyoruz.
            if hasattr(e, "error_dict"):
                for field, errors in e.error_dict.items():
                    for error in errors:
                        self.add_error(field, error)
            else:
                for error in e.error_list:
                    self.add_error(None, error)

        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title:
            RecipeValidator.validate_title(title)
        return title

    def clean_summary(self):
        summary = self.cleaned_data.get("summary")
        if summary:
            RecipeValidator.validate_summary(summary)
        return summary

    def clean_instructions(self):
        instructions = self.cleaned_data.get("instructions")
        if instructions:
            RecipeValidator.validate_instructions(instructions)
        return instructions

    def clean_preparation_time(self):
        prep_time = self.cleaned_data.get("preparation_time")
        if prep_time is not None:
            RecipeValidator.validate_preparation_time(prep_time)
        return prep_time

    def clean_cooking_time(self):
        cook_time = self.cleaned_data.get("cooking_time")
        if cook_time is not None:
            RecipeValidator.validate_cooking_time(cook_time)
        return cook_time

    def clean_servings(self):
        servings = self.cleaned_data.get("servings")
        if servings is not None:
            RecipeValidator.validate_servings(servings)
        return servings
