# Generated by Django 4.2.10 on 2024-03-17 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0074_remove_comment_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
