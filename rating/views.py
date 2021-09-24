from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class SimpleView(View):
    def get(self, request):
        return HttpResponse('hello world!')
