from django.shortcuts import render, HttpResponse

# Тестовая вьюха, только для проверки
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# def test(request):
#     return render(request,  'main/index.html')

# Вьюха мейн пейджа


def main(request):
    return render(request, 'main/index.html')
