from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def logout(request):
    return redirect("login_page")

def register(request):
    return render(request, "register.html")

def add_criminal(request):
    return render(request, "add_criminal.html")

def view_criminal(request):
    return render(request, "view_criminal.html")

def edit_criminal(request):
    return render(request, "edit_criminal.html")

def dashboard(request):
    return render(request, "dashboard.html")

def lodge_complaint(request):
    return render(request, "lodge_complaint.html")

def update_complaint(request):
    return render(request, "update_complaint.html")

def view_complaint(request):
    return render(request, "view_complaint.html")