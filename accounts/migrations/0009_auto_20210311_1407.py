# Generated by Django 3.1.6 on 2021-03-11 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210307_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='propic',
            field=models.ImageField(blank=True, default='media/default.jpg', upload_to='profile_pic'),
        ),
    ]
