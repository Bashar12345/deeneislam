import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

from RED.models import articles

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def api_home(request, *args, **kwargs):
    model_data = articles.objects.all().order_by("?").first()
    data={}
    if model_data:
        data = model_to_dict(model_data)
    return Response(data)
    #return JsonResponse(data)

