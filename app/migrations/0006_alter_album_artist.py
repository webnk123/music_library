# Generated by Django 4.1.3 on 2022-11-15 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_artists_album_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='albums', to='app.artist'),
        ),
    ]
