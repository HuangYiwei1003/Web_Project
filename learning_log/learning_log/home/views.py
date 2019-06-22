from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
def homepage(request):
    """网站的首页"""
    return render(request, 'home/homepage.html')


