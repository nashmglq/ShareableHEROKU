# Generated by Django 4.2.10 on 2024-02-29 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0037_rename_comment_comment_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
