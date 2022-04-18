from django.shortcuts import render

# Create your views here#
from django import views
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    message = 'Congratulations, you have created an API'
    return Response (message)