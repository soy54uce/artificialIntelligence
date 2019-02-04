from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world, welcome to Django Polls")
