# Generated by Django 3.1.6 on 2021-05-26 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210328_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='propic',
            field=models.ImageField(blank=True, default='media/default.png', upload_to='profile_pic'),
        ),
    ]
