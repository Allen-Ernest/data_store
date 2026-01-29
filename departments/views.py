from departments.models import Department
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def all_departments(request):
    departments = Department.objects.all()
    return render(request, "departments.html", {"departments": departments})
    
@login_required
def add_department(request):
    if request.method == 'POST':
        name = request.POST['name']
        code = request.POST['code']
        owner = request.POST['hod']
        if name and code and owner:
            department = Department.objects.create(name=name, code=code, hod=owner)
            department.save()
            return redirect('all_departments')
        else:
            context = {"Error": "Invalid email or password."}
            return redirect('all_departments', context)
        