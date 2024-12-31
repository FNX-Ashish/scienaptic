from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import requests
import json

@api_view(['POST'])
def scienapticcall(request):
    try:
        received_json_data=json.loads(request.body)

        url = 'https://ascendus-uat.scienaptic.com/evaluator/flow/v1/flow-329375952?identifier=f12d499d-2e52-4a81-a659-15cc1a3174ff/'
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        try:
            response = requests.post(url, json=received_json_data, headers=headers)

            if response.status_code == 200:
                output = response.json()
                return JsonResponse({'result': output}, status=200, content_type="application/json")
            else:
                return JsonResponse({'error': 'Failed with status code: ' + str(response.status_code)}, status =response.status_code, content_type="application/json")
        except requests.exceptions.RequestException as err:
            return JsonResponse({'error': str(err)}, status=400, content_type="application/json")

    except Exception as e:
        return JsonResponse({'error': 'Exception occurred: ' + str(e)}, status=400, content_type="application/json")