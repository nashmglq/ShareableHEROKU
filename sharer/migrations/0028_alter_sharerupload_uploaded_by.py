# Generated by Django 4.2.4 on 2024-02-23 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0027_sharerupload_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharerupload',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploads', to='sharer.sharer'),
        ),
    ]