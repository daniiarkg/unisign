from django.shortcuts import render, HttpResponse

# Тестовая вьюха, только для проверки


def test(request):
    return HttpResponse('Hello World')
