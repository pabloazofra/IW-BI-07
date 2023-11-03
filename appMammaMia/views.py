from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime

def index(request):
    year = datetime.now().year
    return render(request, "index.html", {'year': year})