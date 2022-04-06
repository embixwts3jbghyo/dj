from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,FileResponse


def root(req):
    return HttpResponse('''
        <h1>Hello World</h1>
        <p>
            w3school.com is incredible
        </p>
    ''')

# Create your views here.
def json(req):
    data = {
        "name":"django",
        "version":"4.0.3"
    }
    return JsonResponse(data)

