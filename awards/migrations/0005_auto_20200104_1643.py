# Generated by Django 2.2.8 on 2020-01-04 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0004_reviews'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projo_post',
            options={'get_latest_by': 'total', 'ordering': ['posted_on']},
        ),
        migrations.AddField(
            model_name='projo_post',
            name='content',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projo_post',
            name='design',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projo_post',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projo_post',
            name='usability',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.IntegerField()),
                ('usability', models.IntegerField()),
                ('content', models.IntegerField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.projo_post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]