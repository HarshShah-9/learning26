from . import views
from django.urls import path
urlpatterns = [
    path('employeeList/', views.employeeList),
    path('employeeFilter/', views.employeeFilter),
    path('createemployee/',views.createEmployee),
    path('createEmployeeWithForm/',views.createEmployeeWithForm),
    path('createCourse/',views.createCourse),
    path('createDepartment/',views.createDepartment),
    path('createbook/',views.createBook)
]