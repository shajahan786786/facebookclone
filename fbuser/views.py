from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def login(request):
#     return HttpResponse('This is fb module')

def login(request):
    return render(request, 'user_templates/user_login.html')

