from django import http

def home(request):

    return http.HttpResponse('Hello World!\n   Ciao Mondo e tutti! ')