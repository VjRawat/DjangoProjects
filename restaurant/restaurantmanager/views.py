from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

# from restaurantmanager.Forms import AddNewMenu
from .Forms import AddName
from .models import Menu, Name


def index(request):
    template_name = loader.get_template('index.html')
    all_recipes = Menu.objects.all()
    # return HttpResponse("Hello World!")
    context = {
        "tag": "This text is from index.html page.",
        "menus": all_recipes
    }
    return HttpResponse(template_name.render(context, request))

def aboutus(request):
    # return HttpResponse("Thanks for websiting our website.")
    template_name = loader.get_template('aboutus.html')
    context = {
        'tag1': "Hello, welcome to about us page."
    }
    return HttpResponse(template_name.render(context, request))

def detail(request, recipe_name):
    template_name = loader.get_template('menuDetails.html')
    menu_details = Menu.objects.filter(recipe_name=recipe_name)
    context = {
        "details": menu_details
    }
<<<<<<< HEAD

    # return HttpResponse("Display the details of: %s " % recipe_name)
    return HttpResponse(template_name.render(context, request))

def add_new_menu_item(request):
    if request.method == 'POST':
        form = AddName(request.POST)

        if form.is_valid():
            name = request.POST.get('name')
            new_entry = Name(name = name)
            new_entry.save()

    return render(request, 'AddNewMenu.html')
=======
    return HttpResponse(template_name.render(context, request))
>>>>>>> 3d75eec264f97c45711ec92c93e0ab6494c06c82
