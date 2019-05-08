from django.shortcuts import render
from .models import Clients
# Create your views here.

def index(request):
    if "save" in request.GET:
        if "name" not in request.GET or not request.GET['name']:
            return render(request, "template.html", {"error": "Name is required"})

        name = request.GET['name']
        country = request.GET['country']
        birth = request.GET['birth']
        passport = request.GET['passport']
        issue = request.GET['issue']
        expiry = request.GET['expiry']
        email = request.GET['email']
        music = request.GET['music']
        file = request.POST.get('file', False)
        Clients.objects.create(name=name, country=country, birth = birth, passport = passport,
                               issue = issue, expiry = expiry, email = email,
                               music = music, file = file)

    client = Clients.objects.all()
    return render(request, "template.html", {"client": client})

