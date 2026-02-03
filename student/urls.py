from django.urls import path
from . import views

urlpatterns = [
   path("home/",views.studentHome),
   path("dashboard/",views.studentDashboard),
   path("result/",views.studentResult)
]