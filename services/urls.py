from . import views
from django.urls import path
urlpatterns = [
    path('servicesList/', views.servicesList,name="servicesList"),
    path('createServicesWithForm/',views.createServicesWithForm,name="createServicesWithForm"),
    path("deleteServices/<int:id>",views.deleteServices,name="deleteServices"),
    path("updateServices/<int:id>",views.updateServices,name="updateServices")
]