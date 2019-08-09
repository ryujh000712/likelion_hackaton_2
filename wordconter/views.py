from django.shortcuts import render

# Create your views here.

def wchome(request):
    return render(request,'wordcount/wchome.html')