# Generated by Django 2.2.8 on 2020-01-05 15:27

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0005_auto_20200104_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projo_post',
            name='landing_page_pic',
            field=pyuploadcare.dj.models.ImageField(),
        ),
    ]