# Generated by Django 2.0.7 on 2018-08-14 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
