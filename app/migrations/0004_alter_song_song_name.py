# Generated by Django 4.1.3 on 2022-11-15 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_album_name_alter_artist_artist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
