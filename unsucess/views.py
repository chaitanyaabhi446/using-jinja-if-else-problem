from django.shortcuts import render

# Create your views here.

def heartsurgeon(request):
    d={'name':'indu'}
    return render(request,'unsucess.html',d)
