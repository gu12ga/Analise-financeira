import graphene
from django.conf import settings
from api.models import DecFec, Company, StockData, Tendency


class DecFecType(graphene.ObjectType):
    dat_geracao_conjunto_dados = graphene.Date()
    sig_agente = graphene.String()
    num_cnpj = graphene.String()
    ide_conj_und_consumidoras = graphene.Int()
    sc_conj_consumidoras = graphene.String()
    sig_indicador = graphene.String()
    ano_indice = graphene.Int()
    num_periodo_indice = graphene.Int()
    vlr_indice_enviado = graphene.Float()


class CompanyType(graphene.ObjectType):
    ide_conj_und_consumidoras = graphene.Int()
    sc_conj_consumidoras = graphene.String()
    sig_agente = graphene.String()
    num_cnpj = graphene.String()


class StockDataType(graphene.ObjectType):
    company = graphene.Field(CompanyType)
    datetime = graphene.DateTime()
    open = graphene.Float()
    high = graphene.Float()
    low = graphene.Float()
    close = graphene.Float()
    adj_close = graphene.Float()
    volume = graphene.Int()


class TendencyType(graphene.ObjectType):
    company = graphene.Field(CompanyType)
    period = graphene.Int()
    year = graphene.Int()
    tendency = graphene.Float()
    intercept = graphene.Float()


class Query(graphene.ObjectType):
    version = graphene.String()

    def resolve_version(self, info, **kwargs):
        return settings.VERSION

    company = graphene.List(CompanyType)

    def resolve_company(self, info, **kwargs):
        return Company.objects.filter(**kwargs)

    dec_fec = graphene.List(
        DecFecType,
        sig_agente=graphene.String(),
        sig_agente__icontains=graphene.String(),
        dat_geracao_conjunto_dados__gte=graphene.String(),
        dat_geracao_conjunto_dados__lte=graphene.String(),
        num_cnpj=graphene.String(),
        sig_indicador__icontains=graphene.String(),
        num_periodo_indice__gte=graphene.Int(),
        num_periodo_indice__lte=graphene.Int(),
        vlr_indice_enviado__gte=graphene.Float(),
        vlr_indice_enviado__lte=graphene.Float(),
        ano_indice=graphene.Int()
    )
    def resolve_dec_fec(self, info, **kwargs):
        return DecFec.objects.filter(**kwargs)

    dec_fec_count = graphene.Int(
        sig_agente=graphene.String(),
        sig_agente__icontains=graphene.String(),
        at_geracao_conjunto_dados__gte=graphene.String(),
        at_geracao_conjunto_dados__lte=graphene.String(),
        num_cnpj=graphene.String(),
        sig_indicador__icontains=graphene.String(),
        num_periodo_indice__gte=graphene.Int(),
        num_periodo_indice__lte=graphene.Int(),
        vlr_indice_enviado__gte=graphene.Float(),
        vlr_indice_enviado__lte=graphene.Float(),
        ano_indice=graphene.Int()
    )
    def resolve_dec_fec_count(self, info, **kwargs):
        return DecFec.objects.filter(**kwargs).count()

    stock_data = graphene.List(
        StockDataType,
        company__sig_agente=graphene.String(),
        company__ide_conj_und_consumidoras=graphene.Int(),
        company__sc_conj_consumidoras=graphene.String()
    )
    def resolve_stock_data(self, info, **kwargs):
        return StockData.objects.filter(**kwargs)


    tendency = graphene.List(
        TendencyType,
        company__sig_agente=graphene.String(),
        company__ide_conj_und_consumidoras=graphene.Int(),
        company__sc_conj_consumidoras=graphene.String(),
        period=graphene.Int(),
        period__in=graphene.List(graphene.Int),
        period__gte=graphene.Int(),
        period__lte=graphene.Int(),
        year=graphene.Int(),
        year__in=graphene.List(graphene.Int),
        year__gte=graphene.Int(),
        year__lte=graphene.Int(),
    )
    def resolve_tendency(self, info, **kwargs):
        return Tendency.objects.filter(**kwargs)
