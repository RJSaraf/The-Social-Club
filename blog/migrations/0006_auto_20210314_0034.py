# Generated by Django 3.1.6 on 2021-03-13 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210312_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dislike',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='dislike',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]