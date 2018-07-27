# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    context['title'] = 'index page'
    return render(request, 'index.html', context)


# def hello(request):
#    return HttpResponse('Hello world!')


