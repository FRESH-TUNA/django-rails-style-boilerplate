# Generated by Django 3.0.3 on 2020-03-01 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tbs_core_db', '0002_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='url',
            new_name='video_url',
        ),
    ]
