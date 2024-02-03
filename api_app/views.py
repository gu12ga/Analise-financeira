from api_app.models import DecFec
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def consulta(request):

  if request.method == 'POST':

    # Obtenha o JSON do corpo da solicitação
    try:
       json_data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError as e:
      return JsonResponse({'error': f'Erro ao decodificar JSON, {e}'}, status=400)

    consulta = json_data.get('consulta', None)
    parametros = json_data.get('parametros', None)

    resultados = DecFec.consulta_sql(consulta, parametros)     
  
    return JsonResponse({'resultado': resultados}, status=400)

  return JsonResponse({'error': 'Somente métodos POST são permitidos'}, status=405)
