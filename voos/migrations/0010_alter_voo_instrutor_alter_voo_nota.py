# Generated by Django 4.2.1 on 2023-06-22 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_alter_socio_user'),
        ('voos', '0009_alter_voo_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voo',
            name='instrutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.socio'),
        ),
        migrations.AlterField(
            model_name='voo',
            name='nota',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
