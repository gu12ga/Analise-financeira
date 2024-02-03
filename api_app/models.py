from django.db import models, connection

class DecFec(models.Model):
    DatGeracaoConjuntoDados = models.DateField()
    SigAgente = models.CharField(max_length=20)
    NumCNPJ = models.CharField(max_length=14)
    IdeConjUndConsumidoras = models.CharField(max_length=5)
    DscConjUndConsumidoras = models.CharField(max_length=255)
    SigIndicador = models.CharField(max_length=3)
    AnoIndice = models.CharField(max_length=4)
    NumPeriodoIndice = models.IntegerField()
    VlrIndiceEnviado = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        db_table = 'dec_fec'

    def __str__(self):
        return (
            f"DatGeracaoConjuntoDados: {self.DatGeracaoConjuntoDados}, "
            f"SigAgente: {self.SigAgente}, "
            f"NumCNPJ: {self.NumCNPJ}, "
            f"IdeConjUndConsumidoras: {self.IdeConjUndConsumidoras}, "
            f"DscConjUndConsumidoras: {self.DscConjUndConsumidoras}, "
            f"SigIndicador: {self.SigIndicador}, "
            f"AnoIndice: {self.AnoIndice}, "
            f"NumPeriodoIndice: {self.NumPeriodoIndice}, "
            f"VlrIndiceEnviado: {self.VlrIndiceEnviado}"
        )
    
    @classmethod
    def consulta_sql(cls, sql_query, params=None):
        """
        Executa uma consulta SQL e retorna os resultados.

        :param sql_query: String contendo a consulta SQL.
        :param params: Parâmetros seguros para a consulta (opcional).
        :return: Resultados da consulta.
        """
        try:

            with connection.cursor() as cursor:

                if params[0] is not None:
                    cursor.execute(sql_query, params)
                else:
                    cursor.execute(sql_query)

                results = cursor.fetchall()
            return results
        except Exception as e:
            # Handle exceptions or log the error
            print(f"Error executing SQL query: {e}")
            return None
