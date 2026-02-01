from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import User, AdminProfile, ClientProfile
from departments.models import Department
from documents.models import Document
import uuid

def get_client_login(request):
    return render(request, 'user_login.html')

def get_client_register(request):
    departments = Department.objects.all()
    return render(request, 'user_register.html', {'departments': departments})

def client_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None and user.role == 'client':
            login(request, user)
            return redirect('client_dashboard')

        else:
            messages.error(request, 'Email or password incorrect')
            return redirect('client_login')

@login_required
def get_client_dashboard(request):
    user = request.user
    if user.role != 'client':
        return redirect('client_login')
    else:
        email = user.email
        first_name = user.first_name
        middle_name = user.middle_name
        last_name = user.last_name
        department = user.client_profile.department.name
        return render(request, 'user_dashboard.html')
    
@login_required
def get_client_profile(request):
    user = request.user
    if user.role != 'client':
        return redirect('client_login')
    else:
        context = {"email": user.email,
        "first_name": user.first_name,
        "middle_name": user.middle_name,
        "last_name": user.last_name,
        "department" : user.client_profile.department.name
        }
        return render(request, 'user_profile.html', context)

@login_required
def get_client_documents(request):
    user = request.user
    if user.role != 'client':
        return redirect('client_login')
    else:
        documents = user.documents.all()
        return render(request, 'user_documents.html', {'documents': documents})

def client_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        department_id = request.POST.get('department')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        check_num = uuid.uuid4()

        try:
            if password != confirm_password:
                messages.error(request, "Passwords do not match")
                return redirect('client_register')
            department = Department.objects.get(id=department_id)
            user = User.objects.create_user(email=email, password =password, first_name=first_name, middle_name=middle_name, last_name=last_name)
            ClientProfile.objects.create(user=user,check_num=check_num, department=department)
            return redirect('client_login')
        except Department.DoesNotExist:
            return ('client_register')
        
        if password != confirm_password:
            return render(request, 'user_login.html')

def get_admin_login(request):
    return render(request, 'admin_login.html')

def get_admin_register(request):
    return render(request, 'admin_register.html')

def register_admin(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords must match.')
            return render(request, 'admin_login.html')

        user = User.objects.create_user(email=email, password=password, first_name=first_name, middle_name=middle_name, last_name=last_name, role='admin')
        AdminProfile.objects.create(user=user)
        return redirect('admin_login')
    
def login_admin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None and user.role == 'admin':
            login(request, user)
            return redirect('admin_dashboard')
        else:
            context = {"Error": "Invalid email or password."}
            return render(request, 'admin_login.html', context)

@login_required
def admin_dashboard(request):
    user = request.user
    if user.role != 'admin':
        return redirect('admin_login')
    email = user.email
    role = user.role
    first_name = user.first_name
    middle_name = user.middle_name
    last_name = user.last_name
    return render(request, 'admin_dashboard.html')

def logout_admin(request):
    logout(request)
    return redirect('admin_login')

def get_client_logout(request):
    logout(request)
    return redirect('user_login.html')