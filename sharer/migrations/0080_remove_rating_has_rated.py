# Generated by Django 4.2.10 on 2024-03-18 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0079_rating_has_rated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='has_rated',
        ),
    ]