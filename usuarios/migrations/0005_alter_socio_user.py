# Generated by Django 4.2.2 on 2023-06-15 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0004_certificadointrutor_socio_breve_socio_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]