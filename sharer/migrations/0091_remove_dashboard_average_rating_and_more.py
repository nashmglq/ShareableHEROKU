# Generated by Django 4.2.10 on 2024-03-21 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0090_dashboard_average_rating_dashboard_total_likes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard',
            name='average_rating',
        ),
        migrations.RemoveField(
            model_name='dashboard',
            name='total_likes',
        ),
        migrations.RemoveField(
            model_name='dashboard',
            name='total_posts',
        ),
        migrations.RemoveField(
            model_name='dashboard',
            name='total_unlikes',
        ),
        migrations.RemoveField(
            model_name='dashboard',
            name='total_uploads',
        ),
    ]
