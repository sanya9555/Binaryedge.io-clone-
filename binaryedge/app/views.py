from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,AnonymousUser
import requests

def index(request):
    
    return render(request,"app/index.html")

def image(request):
    return render(request,"app/images.html")

def dataleaks(request):

    context={}
    if request.method=="POST":
        try:
            domain=request.POST['domain']
            r=requests.get(f"http://127.0.0.1:8000/dataleaks/{domain}")
            data=r.json[f"{domain}"]

            context={
                'dataleaks':data
            }
        except Exception as e:
            context={
                'dataleaks':"Not Found"
            }
    return render(request,"app/dataleaks.html",context)
def domains(request):

    context={}
    if request.method=="POST":
        try:
            domain=request.POST["subdomain"]
            r=requests.get(f"https://api.hunter.io/v2/domain-search?domain={domain}.com&api_key=136845dd23fad3b769ebe6ea15257f289c7210cf")
            response=r.json()
            data= response.get("data","No data Found")

            context={
                'subdomain':data
            }
        except Exception as e:
            context={
                'subdomain': "Not Found"
            }
    return render(request,"app/domains.html",context)
def sensors(request):
    return render(request,"app/sensors.html")

def torrents(request):
    return render(request,"app/torrents.html")

