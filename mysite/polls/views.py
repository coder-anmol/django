from django.http import HttpResponse


# creating my first view
def index(request):
    return HttpResponse('<h1>Hello, World. You are at polls index.</h1>')
