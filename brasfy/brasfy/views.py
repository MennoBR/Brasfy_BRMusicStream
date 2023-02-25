#definindo as views html:

from django.shortcuts import render


def home(request):
    return render(request, 'brasfy/home.html')
