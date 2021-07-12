from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome to Console Collector</h1>')

def about(request):
    return render(request, 'about.html')

def consoles_index(request):
    return render(request, 'consoles/index.html', { 'consoles': consoles})