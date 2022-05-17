import json
from django.forms.models import model_to_dict
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render,get_object_or_404

from RED.models import articles
from api.serializers import ArticleSerializer

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class article_api_view(viewsets.ModelViewSet):
    queryset = articles.objects.all()
    serializer_class = ArticleSerializer


# Create your views here.
@api_view(['GET'])
def api_home(request, *args, **kwargs):
    model_data = articles.objects.all().order_by("?").first()
    data={}
    if model_data:
        data = model_to_dict(model_data)
    return Response(data)
    #return JsonResponse(data)

