# Generated by Django 4.2.1 on 2023-06-15 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0003_socio_sobrenome_alter_socio_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificadoIntrutor',
            fields=[
                ('socio', models.OneToOneField(limit_choices_to=models.Q(('breve', ''), _negated=True), on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='certificado_instrutor', serialize=False, to='usuarios.socio')),
                ('nome_curso', models.TextField(blank=True, default='', max_length=200, null=True)),
                ('data_diploma', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Graduado em:')),
            ],
        ),
        migrations.AddField(
            model_name='socio',
            name='breve',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='socio',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Documento',
        ),
    ]
