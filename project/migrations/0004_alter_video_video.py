# Generated by Django 4.1.7 on 2023-04-06 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_video_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='video/%y'),
        ),
    ]
