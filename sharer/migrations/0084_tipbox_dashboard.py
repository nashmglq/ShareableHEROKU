# Generated by Django 4.2.10 on 2024-03-21 01:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sharer', '0083_remove_sharerupload_file_remove_sharerupload_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sharer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sharer.sharer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_earnings', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_uploads', models.IntegerField()),
                ('total_likes', models.IntegerField()),
                ('total_comments', models.IntegerField()),
                ('sharer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sharer.sharer')),
            ],
        ),
    ]
