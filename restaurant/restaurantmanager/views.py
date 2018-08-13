from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def index(request):
    template_name = loader.get_template("index.html")
    context = {
        "tag": "This text is from index.html"
    }
    return HttpResponse(template_name.render(context, request))

def aboutus(request):


    return HttpResponse("Thanks fo visiting our website")