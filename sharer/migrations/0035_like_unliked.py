# Generated by Django 4.2.4 on 2024-02-25 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0034_like_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='unliked',
            field=models.BooleanField(default=False),
        ),
    ]