# Generated by Django 5.1.1 on 2024-09-24 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentname',
            name='date_reported',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='studentname',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
