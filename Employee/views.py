from django.shortcuts import render
from .form import EmployeeForm
from .models import Employees

# Create your views here.
def EmployeeDetails(request):
    if request.method == "POST":
        form = EmployeeForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, "home.html", {"obj": obj})
    else:
        form = EmployeeForm()
    return render(request, "empdetails.html", {"form": form})

def ViewEmployees(request):
    if request.method == "GET":
        form = EmployeeForm()
        img = Employees.objects.all()
        return render(request, "viewemployees.html", {"img": img, "form": form})

def getEmployee(request,pid):
    if request.method == "GET":
        form = EmployeeForm()
        img = Employees.objects.get(EmployeeId=pid)
        return render(request, "employee.html", {"img": img, "form": form})

