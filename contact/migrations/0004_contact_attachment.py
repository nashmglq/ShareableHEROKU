# Generated by Django 4.2.10 on 2024-03-15 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_rename_contactrequest_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='contact_attachments'),
        ),
    ]
