from django.urls import path
from .views import EmployeeDetails,ViewEmployees,getEmployee
urlpatterns = [
    path('',EmployeeDetails),
    path('views',ViewEmployees),
    path('employee/<int:pid>',getEmployee)
    ]