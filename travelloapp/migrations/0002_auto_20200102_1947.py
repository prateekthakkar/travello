# Generated by Django 3.0.1 on 2020-01-02 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelloapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='destination',
            name='price',
            field=models.IntegerField(max_length=10),
        ),
    ]
