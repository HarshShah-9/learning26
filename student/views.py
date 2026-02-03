from django.shortcuts import render

# Create your views here.

def studentHome(request):
    return render(request,"student/studentHome.html")
def studentDashboard(request):
    student = {"name":"raj","age":23,"city":"Ahmedabad"}
    return render(request,"student/studentDashboard.html",student)    
def studentResult(request):
    student = {"name":"Rahul","Field":"CSE","Result":"Pass"}
    return render(request,"student/studentResult.html",student) 
   