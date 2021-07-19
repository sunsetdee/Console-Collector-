from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# the below Console variable imported from models is linking to line console_index
# function Console
from .models import Console, Game
from .forms import AccessoryForm, AccessoryForm

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
    games_console_doesnt_have = Game.objects.exclude(id__in = console.games.all().values_list('id'))

    # instantiate FeedForm to be rendered in the template
    accessory_form = AccessoryForm()
    # below the left side 'console' is passing to detail.html to render the data
    return render(request, 'consoles/detail.html', { 'console': console,
        'accessory_form': accessory_form, 'games': games_console_doesnt_have })

class ConsoleCreate(CreateView):
    model = Console
    # the codes below field = '__all__'' is = to this   fields = ['make', 'consolemodel', 'price', 'released_year']
    fields = ['make', 'consolemodel', 'price', 'released_year']
    # codes below redirct to /consoles after adding a new console
    success_url = '/consoles/'

class ConsoleUpdate(UpdateView):
  model = Console
  # Let's disallow the renaming of a console by excluding the make field!
  fields = ['consolemodel', 'price', 'released_year']

class ConsoleDelete(DeleteView):
  model = Console
  success_url = '/consoles/'

def add_accessory(request, console_id):
    # create a ModelForm instance using the data in request.POST
    form = AccessoryForm(request.POST)
    if form.is_valid():
        # the below codes are for assigning a console id first before saving it. That's why we need FORM.SAVE(COMMIT=FALSE), is to 
        # create a console id first but not saving it. creating the console id is for the accessory linking to it.
        # form.save returns a new accessory object that has not been save to the database
        new_accessory = form.save(commit=False)
        # below codes are for linking the accessory to the console id
        new_accessory.console_id = console_id
        # we create this new variable new_accessory because we need a variable to hold the accessory that's been created 
        new_accessory.save()
        # the first argument 'detail' is linking to urls.py console detail path. The second argument left side console_id can be
        # named anything, but we call it console_id because in urls.py detail path, we also named it <int:console_id>. The right 
        # console_id is named console_id is because we call it console_id in this function's second argument. 
    return redirect('detail', console_id=console_id)

    # the below GameList, GameDetail, GameCreate etc... are referring to urls.py
    # path view.GameList.as.view() and etc... so on
class GameList(ListView):
    model = Game

class GameDetail(DetailView):
    model = Game

class GameCreate(CreateView):
    model = Game
    fields = '__all__'

class GameUpdate(UpdateView):
    model = Game
    fields = '__all__'

class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'

def assoc_game(request, console_id, game_id):
    Console.objects.get(id=console_id).games.add(game_id)
    return redirect('detail', console_id=console_id)
    