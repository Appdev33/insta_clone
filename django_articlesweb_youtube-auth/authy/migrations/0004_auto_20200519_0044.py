# Generated by Django 3.0.4 on 2020-05-19 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0003_auto_20200518_2052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='favorite',
            new_name='favorites',
        ),
    ]
