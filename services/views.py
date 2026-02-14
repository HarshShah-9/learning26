from django.shortcuts import render,HttpResponse,redirect
from .models import Services
from django.http import HttpResponse
from .forms import ServiceForm


def servicesList(request):
    services = Services.objects.all().values()
    print(services)
    return render(request,'services/servicesList.html',{"services":services})

def createServicesWithForm(request):
    print(request.method)
    if request.method == "POST":
        form = ServiceForm(request.POST)
        form.save() 
        return redirect("servicesList")
    else:
        
        form = ServiceForm()        
        return render(request,"services/createserviesForm.html",{"form":form})




def deleteServices(request,id):
    print("id from url = ",id)
    Services.objects.filter(id=id).delete()
    return redirect("servicesList") 



def updateServices(request,id):
    services = Services.objects.get(id=id) 
    
    if request.method == "POST":
        form = ServiceForm(request.POST,instance=services)
        form.save()
        return redirect("serviceList")
    else:
        form = ServiceForm(instance=services)    
        return render(request,"services/updateServices.html",{"form":form})