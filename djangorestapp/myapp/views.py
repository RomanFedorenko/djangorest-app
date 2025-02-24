from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
# Create your views here.

def employeeView(request):
    employees = Employee.objects.all().values()  # Converts queryset to a list of dictionaries
    response = {
        'employees': list(employees)
    }
    return JsonResponse(response, safe=False)  # safe=False allows lists to be serialized
