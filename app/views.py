from django.shortcuts import render

# Create your views here.
def badge(request):
    return render(request,'badge.html')