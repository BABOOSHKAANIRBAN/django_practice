from django.http import HttpResponse

# Create your views here.

def dashboard(request):
    return HttpResponse("Movie Collections")
    
def download(request):
    return HttpResponse('Easily download movies')

def watch(request):
    return HttpResponse('Watch all your favorite movies here')
