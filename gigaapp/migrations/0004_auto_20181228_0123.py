# Generated by Django 2.1.4 on 2018-12-27 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gigaapp', '0003_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
    ]
