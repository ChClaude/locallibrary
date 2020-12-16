from django.template.response import TemplateResponse
from django.http import JsonResponse
import json


def index(request):
    response = TemplateResponse(request, 'd3visualizations/index.html', {})
    return response


def dashboard(request):
    response = TemplateResponse(request, 'd3visualizations/dashboard.html', {})
    return response


def read_deviations(request):
    json_data = open('d3visualizations/static/d3visualizations/data/deviations.json')
    data1 = json.load(json_data)  # deserialises it
    data2 = json.dumps(data1)  # json formatted string

    json_data.close()

    return JsonResponse(data1, safe=False)

