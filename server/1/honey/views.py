from django.shortcuts import render
from django.http import HttpResponse
import django
import os
import sys


def home(request):
    return HttpResponse("Hello, honey! django: " + str(django.VERSION))