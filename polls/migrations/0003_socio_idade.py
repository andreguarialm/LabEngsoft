# Generated by Django 4.2.1 on 2023-06-14 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_socio_idade'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='idade',
            field=models.IntegerField(default=0),
        ),
    ]
