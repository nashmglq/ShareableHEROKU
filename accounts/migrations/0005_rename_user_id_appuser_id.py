# Generated by Django 5.0.1 on 2024-02-04 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_appuser_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appuser',
            old_name='user_id',
            new_name='id',
        ),
    ]