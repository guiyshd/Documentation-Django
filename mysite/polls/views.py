from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def login(request):
    return HttpResponse("Login page.")


def register(request):
    return HttpResponse("Register.")