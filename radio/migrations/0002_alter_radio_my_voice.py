# Generated by Django 3.2 on 2021-05-19 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radio',
            name='my_voice',
            field=models.URLField(max_length=2083),
        ),
    ]
