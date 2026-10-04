"""Tag, Cuisine ve Ingredient için ortak servis, queryset ve validator testleri."""

import pytest
from django.core.exceptions import ValidationError

from recipes.constants import (
    MAX_CUISINE_DESCRIPTION_LENGTH,
    MAX_CUISINE_NAME_LENGTH,
    MAX_TAG_DESCRIPTION_LENGTH,
    MAX_TAG_NAME_LENGTH,
    MIN_CUISINE_NAME_LENGTH,
    MIN_TAG_NAME_LENGTH,
)
from recipes.models import Cuisine, Ingredient, Tag
from recipes.services import CuisineService, IngredientService, TagService
from recipes.validators.cuisine_validator import CuisineValidator
from recipes.validators.tag_validator import TagValidator

CASES = [
    pytest.param(Tag, TagService, "tag", id="tag"),
    pytest.param(Cuisine, CuisineService, "cuisine", id="cuisine"),
    pytest.param(Ingredient, IngredientService, "ingredient", id="ingredient"),
]


def _make(model, name, slug, **extra):
    return model.objects.create(name=name, slug=slug, **extra)


@pytest.mark.django_db
@pytest.mark.parametrize(("model", "service", "arg"), CASES)
class TestServices:
    def test_create(self, model, service, arg):
        obj = service.create(name="Deneme", slug="deneme")

        assert obj.pk is not None
        assert model.objects.filter(slug="deneme").exists()

    def test_update_changes_fields(self, model, service, arg):
        obj = _make(model, "Eski", "eski")

        service.update(obj, name="Yeni")

        obj.refresh_from_db()
        assert obj.name == "Yeni"

    def test_update_without_data_is_noop(self, model, service, arg):
        obj = _make(model, "Aynı", "ayni")

        assert service.update(obj) is obj

    def test_activate_and_deactivate(self, model, service, arg):
        obj = _make(model, "Durum", "durum")

        service.deactivate(obj)
        obj.refresh_from_db()
        assert obj.is_active is False

        service.activate(obj)
        obj.refresh_from_db()
        assert obj.is_active is True

    def test_delete(self, model, service, arg):
        obj = _make(model, "Silinecek", "silinecek")

        service.delete(obj)

        assert not model.objects.filter(pk=obj.pk).exists()


@pytest.mark.django_db
@pytest.mark.parametrize(("model", "service", "arg"), CASES)
class TestQuerySets:
    def test_active_and_inactive(self, model, service, arg):
        active = _make(model, "Aktif", "aktif")
        inactive = _make(model, "Pasif", "pasif", is_active=False)

        assert list(model.objects.active()) == [active]
        assert list(model.objects.inactive()) == [inactive]

    def test_sort_by_name(self, model, service, arg):
        b = _make(model, "B", "b-slug")
        a = _make(model, "A", "a-slug")

        assert list(model.objects.sort_by_name()) == [a, b]

    def test_by_slug(self, model, service, arg):
        obj = _make(model, "Bul", "bul")
        _make(model, "Diğer", "diger")

        assert list(model.objects.by_slug("bul")) == [obj]

    def test_search_filters_by_name(self, model, service, arg):
        match = _make(model, "Acılı Ezme", "acili-ezme")
        _make(model, "Baklava", "baklava")

        assert list(model.objects.search("ezme")) == [match]

    def test_blank_search_returns_everything(self, model, service, arg):
        _make(model, "Bir", "bir")
        _make(model, "İki", "iki")

        assert model.objects.search("   ").count() == 2


@pytest.mark.django_db
@pytest.mark.parametrize(("model", "service", "arg"), [CASES[0], CASES[2]])
class TestRecipeCounts:
    def test_has_recipes_and_counts(self, model, service, arg):
        from tests.factories import (
            IngredientFactory,
            RecipeFactory,
            RecipeIngredientFactory,
            TagFactory,
        )

        recipe = RecipeFactory()
        if model is Tag:
            used = TagFactory()
            unused = TagFactory()
            from recipes.models import RecipeTag

            RecipeTag.objects.create(recipe=recipe, tag=used)
        else:
            used = IngredientFactory()
            unused = IngredientFactory()
            RecipeIngredientFactory(recipe=recipe, ingredient=used)

        assert list(model.objects.has_recipes()) == [used]
        assert unused not in model.objects.active_with_recipes()

        counts = {o.pk: o.recipe_count for o in model.objects.active_with_recipe_count()}
        assert counts[used.pk] == 1
        assert counts[unused.pk] == 0


@pytest.mark.parametrize(
    ("validator", "min_len", "max_len", "max_desc"),
    [
        pytest.param(
            TagValidator, MIN_TAG_NAME_LENGTH, MAX_TAG_NAME_LENGTH,
            MAX_TAG_DESCRIPTION_LENGTH, id="tag",
        ),
        pytest.param(
            CuisineValidator, MIN_CUISINE_NAME_LENGTH, MAX_CUISINE_NAME_LENGTH,
            MAX_CUISINE_DESCRIPTION_LENGTH, id="cuisine",
        ),
    ],
)
class TestNamedValidators:
    def test_name_bounds(self, validator, min_len, max_len, max_desc):
        validator.validate_name("a" * min_len)
        validator.validate_name("a" * max_len)

        with pytest.raises(ValidationError):
            validator.validate_name("a" * (min_len - 1))
        with pytest.raises(ValidationError):
            validator.validate_name("a" * (max_len + 1))

    def test_name_required(self, validator, min_len, max_len, max_desc):
        for bad in (None, "", "   "):
            with pytest.raises(ValidationError):
                validator.validate_name(bad)

    def test_description_optional_but_limited(self, validator, min_len, max_len, max_desc):
        validator.validate_description("")
        validator.validate_description("a" * max_desc)

        with pytest.raises(ValidationError):
            validator.validate_description("a" * (max_desc + 1))

    def test_is_active_must_be_bool(self, validator, min_len, max_len, max_desc):
        validator.validate_is_active(True)

        with pytest.raises(ValidationError):
            validator.validate_is_active("evet")

    def test_validate_data_checks_only_given_keys(self, validator, min_len, max_len, max_desc):
        method = (
            validator.validate_tag_data
            if validator is TagValidator
            else validator.validate_cuisine_data
        )

        method({})
        method({"name": "Geçerli", "description": "", "is_active": True})

        with pytest.raises(ValidationError):
            method({"name": ""})
