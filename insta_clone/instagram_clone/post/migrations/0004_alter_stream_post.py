# Generated by Django 4.0.6 on 2022-08-14 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
    ]
