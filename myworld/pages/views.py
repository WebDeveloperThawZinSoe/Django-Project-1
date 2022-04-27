from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    context = {
    'title': 'Home Page',
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('about.html')
    context = {
        'title': 'About Page',
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template('contact.html')
    context = {
        'title': 'Contact Page',
    }
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('login.html')
    context = {
        'title': 'Login Page',
    }
    return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template('register.html')
    context = {
        'title': 'Register Page',
    }
    return HttpResponse(template.render(context, request))