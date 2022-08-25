import http
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    return HttpResponse("This is the polls index")


