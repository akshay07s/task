# Generated by Django 3.1.4 on 2020-12-27 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='', max_length=50),
        ),
    ]
