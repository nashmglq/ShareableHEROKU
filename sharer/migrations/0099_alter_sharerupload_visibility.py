# Generated by Django 4.2.10 on 2024-03-25 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0098_remove_sharer_followers_tier1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharerupload',
            name='visibility',
            field=models.CharField(choices=[('ALL', 'All (followers and non-followers)'), ('FOLLOWERS_TIER1', 'Followers - Tier 1'), ('FOLLOWERS_TIER2', 'Followers - Tier 2'), ('FOLLOWERS_TIER3', 'Followers - Tier 3')], default='ALL', max_length=20),
        ),
    ]
