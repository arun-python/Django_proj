from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Datas
# Create your views here.
def home(request):
    mydata= Datas.objects.all()
    if mydata!= '':
        return render(request, "home.html", {'accessdata':mydata})

    else:
        return render(request, "home.html")

def addData(request):
    if request.method=='POST':
        inputname= request.POST['name']
        inputage= request.POST['age']
        inputaddress= request.POST['address']
        inputcontact= request.POST['contact']
        inputemail= request.POST['email']

        obj=Datas()
        obj.Name= inputname
        obj.Age=inputage
        obj.Address= inputaddress
        obj.Contact= inputcontact
        obj.Email= inputemail
        obj.save()
        mydata= Datas.objects.all()
        return redirect("home")
    return render(request, "home.html")   

def updateData(request,id):
    mydata=Datas.objects.get(id=id)
    if request.method=="POST":
        inputname= request.POST['name']
        inputage= request.POST['age']
        inputaddress= request.POST['address']
        inputcontact= request.POST['contact']
        inputemail= request.POST['email']

        mydata.Name= inputname
        mydata.Age=inputage
        mydata.Address= inputaddress
        mydata.Contact= inputcontact
        mydata.Email= inputemail
        mydata.save()
        return redirect("home")
    return render(request,"update.html", {'data':mydata}) 

def deleteData(request,id):
    mydata=Datas.objects.get(id=id)
    mydata.delete()
    return redirect("home")
