# Generated by Django 4.0.6 on 2022-08-17 12:29

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_likes_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(null=True, upload_to=post.models.user_directory_path, verbose_name='Picture'),
        ),
    ]
