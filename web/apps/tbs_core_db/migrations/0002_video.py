# Generated by Django 3.0.3 on 2020-02-29 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tbs_core_db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.FileField(upload_to='user_videos/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
