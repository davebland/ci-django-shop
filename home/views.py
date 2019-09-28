from django.shortcuts import render

def index(request):
    """ Return index page view """
    return render(request, 'index.html')