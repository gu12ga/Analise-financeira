from api_app.models import *
from django.db import transaction
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def insercao_teste(request):

  if request.method == 'POST':

    print("Antes de ler e inserir")

    insert_empresa(('123123', 'GUGA'))

    print("Depois de ler e inserir") 
    
    return JsonResponse({'resultado': 'ocorreu de forma correta'}, status=400)

  return JsonResponse({'error': 'Somente métodos POST são permitidos'}, status=405)


@csrf_exempt
def insercao(request):

  if request.method == 'POST':

    print("Antes de ler e inserir")

    lerCSV_Inserir() 

    print("Depois de ler e inserir") 
    
    return JsonResponse({'resultado': 'ocorreu de forma correta'}, status=400)

  return JsonResponse({'error': 'Somente métodos POST são permitidos'}, status=405)

def lerCSV_Inserir():

        def converter_para_numero(valor):
            try:
                v_teste = valor.replace(',', '').replace('\r\n', '').replace('\n', '')
                vl = ''

                vl_list = list(v_teste)

                if len(vl_list) == 2:
                    vl = f'{vl_list[0]}.{vl_list[1]}'
                    return float(vl)
                else:
                    vl = valor.replace(',', '.').replace('\r\n', '').replace('\n', '')
                    return float(vl)

            except ValueError:
                return None

        errors = []
        rows = []
        aux = True
        aux2 = True

        print("Antes de ler CSV")
        with open('/home/gustavo/Área de Trabalho/Analise/dados/indicadores-conformidade-nivel-tensao.csv', 'rb') as fz:
            data = fz.readlines()
            
        for row in data:
            try:
                decoded = row.decode('utf-8')
            except Exception as e:
                errors.append(row)
                continue

            # Assuming you want to replace 'Vrin' with an empty string and split by ';'
            cleaned_row = decoded.replace('Vrin', '').split(';')
            
            print(cleaned_row[7])
            if not aux and converter_para_numero(cleaned_row[7])>0:
                rows.append(cleaned_row)
            
            aux = False
            
        
        clean_errors = []

        for error in errors:
          row = ''.join(chr(i) for i in error[:-2])
          row_split = row.split(';')
          print(row_split[7])
          if converter_para_numero(row_split[7])>0:
                clean_errors.append(row.split(';'))
          
        #print("Antes de adicioanr linhas")
        print(f'Teste tamanho clean_errors:{len(clean_errors)}')
        print(f'Teste tamanho rows:{len(rows)}')
        print(f'Teste tamanho:{(len(rows)+len(clean_errors))}')
        print(f'Teste rows primeiro: {rows[1]}')
        print(f'Teste clean_errors primeiro: {clean_errors[1]}')
        #adicionarLinhas(rows, clean_errors)

def adicionarLinhas(rows, clean_errors):
  
    print("Antes de adicionar às listas")
    empresas = []
    anos = []
    consumidor = []
    dec_fec = []

    def converter_para_numero(valor):
        try:
            v_teste = valor.replace(',', '').replace('\r\n', '').replace('\n', '')
            vl = ''

            vl_list = list(v_teste)

            if len(vl_list) == 2:
                vl = f'{vl_list[0]}.{vl_list[1]}'
                return float(vl)
            else:
                vl = valor.replace(',', '.').replace('\r\n', '').replace('\n', '')
                return float(vl)

        except ValueError:
            return None

    print("Antes de inserir os dados")

    aux = True

    for row in rows:

        if aux:
            aux = False
            continue
        try:
            if (row[1], row[2]) not in empresas:
                #print("Teste empresa")
                empresas.append((row[1], row[2]))
                insert_empresa((row[1], row[2]))

            if((row[6], row[7]) not in anos):
                #print("Teste anos")
                anos.append((row[6], row[7]))
                insert_ano((row[6], row[7]))

            if (row[3], row[4]) not in consumidor:
                #print("Teste consumidor")
                consumidor.append((row[3], row[4]))
                insert_consumidor((row[3], row[4]))
        
            if (get_empresa(row[2]).id_empresa, row[5], get_ano(row[6], row[7]).id_ano, converter_para_numero(row[8]), row[3]) not in dec_fec:
                #print("Teste dec_fec")
                if(converter_para_numero(row[8])>float(20)):
                    print(row[8])
                dec_fec.append((get_empresa(row[2]).id_empresa, row[5], get_ano(row[6], row[7]).id_ano, converter_para_numero(row[8]), row[3]))
                insert_dec_fec((row[2], row[5], row[6], row[7], converter_para_numero(row[8]), row[3]))
        
        except Exception as e:
            print(e)

    for row in clean_errors:

        if aux:
            aux = False
            continue
        try:
            if (row[1], row[2]) not in empresas and get_empresa(row[2]) == None:
                #print("Teste empresa")
                empresas.append((row[1], row[2]))
                insert_empresa((row[1], row[2]))

            if((row[6], row[7]) not in anos and get_ano((row[6], row[7])) == None):
                #print("Teste anos")
                anos.append((row[6], row[7]))
                insert_ano((row[6], row[7]))

            if (row[3], row[4]) not in consumidor and get_consumidoras(row[3]) == None:
                #print("Teste consumidor")
                consumidor.append((row[3], row[4]))
                insert_consumidor((row[3], row[4]))
        
            if (get_empresa(row[2]).id_empresa, row[5], get_ano(row[6], row[7]).id_ano, converter_para_numero(row[8]), row[3]) not in dec_fec:
                #print("Teste dec_fec")
                dec_fec.append((get_empresa(row[2]).id_empresa, row[5], get_ano(row[6], row[7]).id_ano, converter_para_numero(row[8]), rows[3]))
                insert_dec_fec((row[2], row[5], row[6], row[7], converter_para_numero(row[8]), row[3]))
        except Exception as e:
            print(e)
        
    print("Depois de ter inserido eles")

@transaction.atomic
def insert_empresa(data):
    try:
        Empresa.objects.create(
            sig_agente=data[0],
            cnpj=data[1]
        )
    except IntegrityError as e:
        print(f"Erro ao inserir empresa: {e}")
    except Exception as e:
        print(f"Erro não esperado ao inserir empresa: {e}")

@transaction.atomic
def get_empresa(num_cnpj):
    try:
        empresa = Empresa.objects.filter(cnpj=num_cnpj).first()
        return empresa if empresa else None
    except Exception as e:
        print(f"Erro ao buscar empresa: {e}")
        return None

@transaction.atomic
def insert_ano(data):
    try:
        Ano.objects.create(
            ano=int(data[0]),
            periodo=int(data[1])
        )
    except IntegrityError as e:
        print(f"Erro ao inserir ano: {e}")
    except Exception as e:
        print(f"Erro não esperado ao inserir ano: {e}")

@transaction.atomic
def get_ano(ano, periodo):
    try:
        ano_obj = Ano.objects.filter(ano=int(ano), periodo=int(periodo)).first()
        return ano_obj if ano_obj else None
    except Exception as e:
        print(f"Erro ao buscar ano: {e}")
        return None

@transaction.atomic
def insert_consumidor(data):
    try:
        Consumidor.objects.create(
            id_consumidoras=int(data[0]),
            descricao=data[1]
        )
    except IntegrityError as e:
        print(f"Erro ao inserir consumidor: {e}")
    except Exception as e:
        print(f"Erro não esperado ao inserir consumidor: {e}")

@transaction.atomic
def get_consumidoras(id):
    try:
        consumidoras = Consumidor.objects.filter(id_consumidoras=int(id)).first()
        return consumidoras if consumidoras else None
    except Exception as e:
        print(f"Erro ao buscar ano: {e}")
        return None

@transaction.atomic
def insert_dec_fec(data):
    try:
        empresa = get_empresa(data[0])
        ano = get_ano(data[2], data[3])
        consumidor = get_consumidoras(data[5])
        #print(empresa)
        #print(ano)
        DecFec.objects.create(
            empresa=empresa,
            sig_indicador=data[1],
            ano=ano,
            vlr_indice=data[4],
            consumidoras=consumidor
        )
    except IntegrityError as e:
        print(f"Erro ao inserir DecFec: {e}")
    except Exception as e:
        print(f"Erro não esperado ao inserir DecFec: {e}")

@transaction.atomic
def insert_ano_consumidor(data):
    try:
        for row in data:
            AnoConsumidor.objects.create(
                id=row[0],
                id_ano=row[1],
                ideconjundconsumidoras=row[2],
                id_empresa=row[3]
            )
    except IntegrityError as e:
        print(f"Erro ao inserir AnoConsumidor: {e}")
    except Exception as e:
        print(f"Erro não esperado ao inserir AnoConsumidor: {e}")

@transaction.atomic
def insert_dec_fec_consumidor(data):
    try:
        for row in data:
            DecFecConsumidor.objects.create(
                id_consumidoras=row[0],
                id_dec_fec=row[1]
            )
    except IntegrityError as e:
        print(f"Erro ao inserir DecFecConsumidor: {e}")
    except Exception as e:
        print(f"Erro não esperado ao inserir DecFecConsumidor: {e}")
