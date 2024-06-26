# Generated by Django 4.2.10 on 2024-03-13 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0063_alter_sharer_category'),
        ('accounts', '0022_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='sharer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='sharer.sharer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
