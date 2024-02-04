# Generated by Django 2.1.4 on 2024-02-03 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DecFec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat_geracao_conjunto_dados', models.DateField()),
                ('sig_agente', models.CharField(max_length=255)),
                ('num_cnpj', models.CharField(max_length=255)),
                ('ide_conj_und_consumidoras', models.IntegerField()),
                ('sc_conj_consumidoras', models.CharField(max_length=255)),
                ('sig_indicador', models.CharField(max_length=255)),
                ('ano_indice', models.IntegerField()),
                ('num_periodo_indice', models.IntegerField()),
                ('vlr_indice_enviado', models.FloatField()),
            ],
        ),
    ]