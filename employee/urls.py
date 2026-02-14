from . import views
from django.urls import path
urlpatterns = [
    path('employeeList/', views.employeeList,name="employeeList"),
    path('employeeFilter/', views.employeeFilter),
    path('createemployee/',views.createEmployee),
    path('createEmployeeWithForm/',views.createEmployeeWithForm,name="createEmployeeWithForm"),
    path('createCourse/',views.createCourse),
    path('createDepartment/',views.createDepartment),
    path('createbook/',views.createBook),
    path("deleteEmployee/<int:id>",views.deleteEmployee,name="deleteEmployee"),
    path("filterEmployee/",views.filterEmployee,name="filterEmployee"),
    path("sortEmployee/<int:id>",views.sortEmployee,name="sortEmployee"),
    path("updateemployee/<int:id>",views.updateEmployee,name="updateEmployee")
]