from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    queryset = Emergency.objects.all()
    return render(request, "index.html", {'queryset': queryset})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = User.objects.filter(username=username)
        if user:
            user = authenticate(request, username=username, password=password)
            
            if user:
                login(request, user)
                return redirect('dashboard')
            
        
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect("login_page")

def register_user(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        
        if User.objects.filter(username=username):
            pass
        
        user = User.objects.create(username=username, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        
        LoginMaster.objects.create(user=user,mobile_no=mobile,address=address)
        
        return redirect('login')
        
    return render(request, "register.html")

def add_criminal(request):
    stat = ["Arrested", "In Custody", "Released", "On Bail", "Wanted"]
    
    if request.method == "POST":
        name = request.POST.get('fname')+request.POST.get('lname')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        level = request.POST.get('level')
        status = request.POST.get('status')
        criminal_picture = request.FILES.get('file')
        
        
        CriminalMaster.objects.create(name=name, age=age, status=status, gender=gender, height=height, weight=weight, level=level, criminal_picture=criminal_picture)
        
        return redirect('view_criminal')
        
    return render(request, "add_criminal.html", { "stat": stat })

def view_criminal(request):
    queryset = CriminalMaster.objects.all()
    return render(request, "view_criminal.html", {'queryset': queryset})

def edit_criminal(request, criminal_id):
    criminal = get_object_or_404(CriminalMaster, id=criminal_id)
    
    if request.method == 'POST':
        criminal.name = request.POST.get('name')
        criminal.age = request.POST.get('age')
        criminal.gender = request.POST.get('gender')
        criminal.height = request.POST.get('height')
        criminal.weight = request.POST.get('weight')
        criminal.level = request.POST.get('level')
        criminal.status = request.POST.get('status')
        if request.FILES.get('file'):
            criminal.criminal_picture = request.FILES.get('file')
        criminal.save()
        
        return redirect('view_criminal')
    return render(request, "edit_criminal.html", {'criminal': criminal})

def dashboard(request):
    if request.user.is_superuser:
        all_stations = PoliceStationMaster.objects.all()
        return render(request, "dashboard.html", {'all_stations': all_stations})
    
    else:
        station = PoliceStationMaster.objects.filter(police_station_head=request.user.username)
        if station:
            station = PoliceStationMaster.objects.filter(police_station_head=request.user.username)
            all_complaints = Complaint.objects.filter(p_id=station)
            return render(request, "dashboard.html", {'all_complaints': all_complaints, 'police':True})
        return render(request, "dashboard.html")

def lodge_complaint(request):
    stat = PoliceStationMaster.objects.all()
    if request.method == "POST":
        description = request.POST.get('description')
        station = request.POST.get('station')
        
        p_id = PoliceStationMaster.objects.get(id=station)
        
        Complaint.objects.create(user=request.user, description=description, p_id=p_id)
        
        return redirect('view_complaint')
    return render(request, "lodge_complaint.html", {"stat": stat})

def update_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    choices = ["Pending", "In Progress", "Resolved", "Rejected"]
    
    if request.method == "POST":
        complaint.status = request.POST.get('status')
        complaint.save()
        
        return redirect('view_complaint')

    return render(request, "update_complaint.html", {'complaint': complaint, "stat": choices})

def view_complaint(request):
    queryset = Complaint.objects.filter(user=request.user)
    return render(request, "view_complaint.html", {'queryset': queryset})