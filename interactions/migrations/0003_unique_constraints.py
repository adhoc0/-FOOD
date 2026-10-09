from django.db import migrations, models


class Migration(migrations.Migration):
    """unique_together yerine adlandırılmış UniqueConstraint (aynı kural, yeni API)."""

    dependencies = [
        ("interactions", "0002_rating_rating_score_between_one_and_five"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="favorite",
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name="rating",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="favorite",
            constraint=models.UniqueConstraint(
                fields=("user", "recipe"),
                name="favorite_unique_user_recipe",
            ),
        ),
        migrations.AddConstraint(
            model_name="rating",
            constraint=models.UniqueConstraint(
                fields=("user", "recipe"),
                name="rating_unique_user_recipe",
            ),
        ),
    ]
