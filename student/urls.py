from django.urls import path
from . import views

urlpatterns = [
   path("home/",views.studentHome),
   path("dashboard/",views.studentDashboard),
   path("result/",views.studentResult),
   path("serviceList/",views.serviceList,name="serviceList"),
   path("createService/",views.createService,name="createService"),
   path("delete/<int:id>/",views.deleteService,name="deleteService")
]