# Generated by Django 3.1.6 on 2021-03-25 15:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_auto_20210316_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dislike',
            field=models.ManyToManyField(null=True, related_name='dislikepost', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(null=True, related_name='likepost', to=settings.AUTH_USER_MODEL),
        ),
    ]
