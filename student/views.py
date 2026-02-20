from django.shortcuts import render,get_object_or_404,redirect
from .models import Service
from .forms import ServiceForm

# Create your views here.

def studentHome(request):
    return render(request,"student/studentHome.html")
def studentDashboard(request):
    student = {"name":"raj","age":23,"city":"Ahmedabad"}
    return render(request,"student/studentDashboard.html",student)    
def studentResult(request):
    student = {"name":"Rahul","Field":"CSE","Result":"Pass"}
    return render(request,"student/studentResult.html",student) 

def serviceList(request):
    services = Service.objects.all()
    return render(request,"student/serviceList.html",{"services":services})

def createService(request):

    if request.method =="POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("serviceList")
        else:
            return render(request,"student/createService.html",{"form":form})    
    else:
        form = ServiceForm()
        return render(request,"student/createService.html",{"form":form})

def deleteService(request,id):
    service=get_object_or_404(Service,id=id)
    service.delete()
    return redirect('serviceList')