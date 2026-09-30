from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipeimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='comment_count',
        ),
    ]
