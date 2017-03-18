from django.shortcuts import render
from django.http import HttpResponse


def user_view(request):
    if request.method == 'POST':
        return HttpResponse('hello world.')
    else:
        return HttpResponse('error.')
