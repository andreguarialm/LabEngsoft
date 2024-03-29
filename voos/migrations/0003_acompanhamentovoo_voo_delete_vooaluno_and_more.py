# Generated by Django 4.2.1 on 2023-06-15 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_certificadointrutor_socio_breve_socio_user_and_more'),
        ('voos', '0002_alter_vooaluno_hora_chegada_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcompanhamentoVoo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField()),
                ('parecer', models.TextField()),
                ('instrutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.socio')),
            ],
        ),
        migrations.CreateModel(
            name='Voo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora_chegada', models.TimeField()),
                ('hora_saida', models.TimeField()),
                ('socio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.socio')),
            ],
        ),
        migrations.DeleteModel(
            name='VooAluno',
        ),
        migrations.DeleteModel(
            name='VooPiloto',
        ),
        migrations.AddField(
            model_name='acompanhamentovoo',
            name='voo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='voos.voo'),
        ),
    ]
