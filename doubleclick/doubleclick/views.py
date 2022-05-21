from django.http import HttpResponse
from django.shortcuts import render
def about(request):
    return HttpResponse('This is about page')
def home(request):
    return render(request, 'home.html')
def engine(request):
    return render(request, 'engine.html')
def vehicle(request):
    return render(request, 'vehicle.html')
def brake(request):
    return render(request, 'brake.html')
def ac(request):
    return render(request, 'ac.html')
def price(request):
    return render(request, 'price.html')
def wait(request):
    return render(request, 'wait.html')
def cont(request):
    return render(request, 'cont.html')
def history(request):
    return render(request, 'history.html')
def team(request):
    return render(request, 'team.html')
def news(request):
    return render(request, 'news.html')
def promo(request):
    return render(request, 'promo.html')
def launch(request):
    return render(request, 'launch.html')

