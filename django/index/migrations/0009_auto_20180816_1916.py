# Generated by Django 2.0.7 on 2018-08-16 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20180814_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='state',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
