from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# the below Console variable imported from models is linking to line console_index
# function Console
from .models import Console

# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome to Console Collector</h1>')

def about(request):
    return render(request, 'about.html')

def consoles_index(request):
    consoles = Console.objects.all()
    # the 'consoles:' is passing it to the index.html for loop consoles variable
    return render(request, 'consoles/index.html', { 'consoles': consoles})

def consoles_detail(request, console_id):
    console = Console.objects.get(id=console_id)
    # below the left side 'console' is passing to detail.html to render the data
    return render(request, 'consoles/detail.html', { 'console': console })

class ConsoleCreate(CreateView):
    model = Console
    # the codes below field = '__all__'' is = to this   fields = ['make', 'consolemodel', 'price', 'released_year']
    fields = '__all__'
    # codes below redirct to /consoles after adding a new console
    success_url = '/consoles/'

class ConsoleUpdate(UpdateView):
  model = Console
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['consolemodel', 'price', 'released_year']

class ConsoleDelete(DeleteView):
  model = Console
  success_url = '/consoles/'
    