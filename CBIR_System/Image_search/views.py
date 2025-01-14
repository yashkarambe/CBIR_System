from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Page is working")
    return render(request , 'index.html')

def Search(request):
    return render(request, 'Search.html')