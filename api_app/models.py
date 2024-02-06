from django.db import models

class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    sig_agente = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=20)

    class Meta:
        db_table = 'empresa'

class Ano(models.Model):
    id_ano = models.AutoField(primary_key=True)
    ano = models.IntegerField()
    periodo = models.IntegerField()

    class Meta:
        db_table = 'ano'

class Consumidor(models.Model):
    id_consumidoras = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=255)
    class Meta:
        db_table = 'consumidor'

class DecFec(models.Model):
    id_dec_fec = models.AutoField(primary_key=True)
    consumidoras = models.ForeignKey(Consumidor, on_delete=models.CASCADE)
    sig_indicador = models.CharField(max_length=255)
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    vlr_indice = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        db_table = 'dec_fec'

class AnoConsumidor(models.Model):
    id = models.AutoField(primary_key=True)
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE)
    consumidoras = models.ForeignKey(Consumidor, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    class Meta:
        db_table = 'ano_consumidor'

class DadosAcoes(models.Model):
    id = models.AutoField(primary_key=True)
    Date = models.DateField()
    Open = models.DecimalField(max_digits=18, decimal_places=15)
    High = models.DecimalField(max_digits=18, decimal_places=15)
    Low = models.DecimalField(max_digits=18, decimal_places=15)
    Close = models.DecimalField(max_digits=18, decimal_places=15)
    Adj_Close = models.DecimalField(max_digits=18, decimal_places=15)
    Volume = models.IntegerField()
    class Meta:
        db_table = 'dados_acoes'
        
class DadosAcoesEmpresa(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    dados_acoes = models.ForeignKey(DadosAcoes, on_delete=models.CASCADE)

    class Meta:
        db_table = 'dados_acoes_empresa'
        unique_together = ('empresa', 'dados_acoes')

class DadosAcoesInclinacao(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE)
    inclinacao = models.DecimalField(max_digits=20, decimal_places=17)

    class Meta:
        db_table = 'dados_acoes_inclinacao'
        unique_together = ('empresa', 'ano')

class Correlacao(models.Model):
    id_correlacao = models.AutoField(primary_key=True)
    dec_fec = models.ForeignKey(DecFec, on_delete=models.CASCADE)
    kendall = models.DecimalField(max_digits=11, decimal_places=10)
    spearman = models.DecimalField(max_digits=11, decimal_places=10)
    class Meta:
        db_table = 'correlacao'