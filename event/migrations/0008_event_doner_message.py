# Generated by Django 5.0.7 on 2025-01-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_alter_event_location_alter_event_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='doner_message',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
