from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'index.html')

def submit_view(request):
    return render(request,'submit.html')

def sorted_view(request):
    return render(request,'sorted.html')

def boasts_view(request):
    return render(request,'boasts.html')
    # THIS IS THE VIEW FOR BOASTS ONLY

def roasts_view(request):
    return render(request,'roasts.html')
    # THIS IS THE VIEW FOR ROASTS ONLY