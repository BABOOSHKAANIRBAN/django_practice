from django.http import HttpResponse

# Create your views here.

def menu(request):
    return HttpResponse('This is the Games App')

def newgame(request):
    return HttpResponse("You can start a new game here")
