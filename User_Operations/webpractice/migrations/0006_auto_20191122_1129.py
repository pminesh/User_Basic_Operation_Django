# Generated by Django 2.2.4 on 2019-11-22 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpractice', '0005_auto_20191122_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
