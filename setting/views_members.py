from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.


def members(request):
    return render(request, "members.html")