# Generated by Django 2.1.7 on 2019-04-10 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='phone',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
