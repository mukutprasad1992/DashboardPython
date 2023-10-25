from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
