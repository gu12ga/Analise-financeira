from django.db import models


class DecFec(models.Model):
    dat_geracao_conjunto_dados = models.DateField()
    sig_agente = models.CharField(max_length=255)
    num_cnpj = models.CharField(max_length=255)
    ide_conj_und_consumidoras = models.IntegerField()
    sc_conj_consumidoras = models.CharField(max_length=255)
    sig_indicador = models.CharField(max_length=255)
    ano_indice = models.IntegerField()
    num_periodo_indice = models.IntegerField()
    vlr_indice_enviado = models.FloatField()


class Company(models.Model):
    sig_agente = models.CharField(max_length=255)
    num_cnpj = models.CharField(max_length=255)
    ide_conj_und_consumidoras = models.IntegerField()
    sc_conj_consumidoras = models.CharField(max_length=255)


class StockData(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
    volume = models.IntegerField()


class DecFecPeriod(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    period = models.IntegerField()
    mean_score = models.FloatField()
    ewm_score = models.FloatField()


class DecFecYear(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.IntegerField()
    mean_score = models.FloatField()
    ewm_score = models.FloatField()


class Tendency(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    period = models.IntegerField()
    year = models.IntegerField()
    tendency = models.FloatField()
    intercept = models.FloatField()
