# Generated by Django 4.2.1 on 2023-06-21 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voos', '0007_alter_voo_instrutor_alter_voo_nota_alter_voo_parecer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voo',
            name='nota',
            field=models.FloatField(null=True),
        ),
    ]
