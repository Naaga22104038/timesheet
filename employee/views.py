"""This view.py will help to perform backend works """
#pylint: disable=inconsistent-return-statements
#pylint: disable=wrong-import-order
#pylint: disable=ungrouped-imports
#pylint: disable=missing-function-docstring
#pylint: disable=unused-import
#pylint: disable=no-member
#pylint: disable=bad-whitespace
#pylint: disable=no-else-return
#pylint: disable=bad-continuation
#pylint: disable=missing-module-docstring
#pylint: disable=missing-class-docstring
#pylint: disable=trailing-newlines
#pylint: disable=missing-final-newline
#pylint: disable=invalid-name
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee
#This method will retur the home page
def index(request):
    return render(request, 'index.html')

#this methoda helps to uodate the details in the employee
def employees(request):
    if request.method == 'POST' :
        emp_id = request.POST['emp_id']
        emp_name = request.POST['emp_name']
        project_id = request.POST['ProjectId']
        date_time_in = request.POST['date_time_in']
        date_time_out = request.POST['date_time_out']
        duration = request.POST['duration']
        # hourly_rate = request.POST['hourly_rate']
        employee = Employee(emp_id=emp_id,
            emp_name=emp_name,
            ProjectId_id =project_id,
            date_time_in=date_time_in,
            date_time_out=date_time_out,
            duration=duration)
        employee.save()
        messages.success(request, 'Time Sheet added successfully')
        return redirect('/roles/userdashboard')

def testcallback():
    return 'success'
