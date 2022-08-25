from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is the News index.")

def latest(request):
    return HttpResponse("Watch the latest news right now")



