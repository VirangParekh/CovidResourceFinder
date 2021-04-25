from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import request
from .models import Patient, Institution, PatientFiles, User
from .forms import PatientSignUpForm, PatientFurtherDetailsForm, InstituteSignUpForm
from django.contrib import messages

# Create your views here.


def PatientSignUpView(request):
    if request.method == "POST":
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request=request, user=user)
            return redirect("/resource_finder/accounts/patient_home")
    else:
        form = PatientSignUpForm()
    return render(request, "ResourceFinderApp/SignUpPatient.html", {"form": form})


def InstituteSignUpView(request):
    if request.method == "POST":
        form = InstituteSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request=request, user=user)
            return redirect("/resource_finder/accounts/patient_home")
    else:
        form = InstituteSignUpForm()
    return render(request, "ResourceFinderApp/SignUpInstitute.html", {"form": form})


def LoginView(request):
    if request.user.is_authenticated:
        if request.user.is_patient:
            return redirect("/resource_finder/accounts/patient_home")
        if request.user.is_institution:
            return redirect("/resource_finder/accounts/institute_home")
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(
            request=request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            logged_in_user = User.objects.get(username=username)
            if logged_in_user.is_patient:
                return redirect("/resource_finder/patient_home")
            if logged_in_user.is_institution:
                return redirect("/resource_finder/institute_home")
        else:
            messages.error(request, "username or password not correct")
            return redirect("login")
    else:
        form = AuthenticationForm()
    return render(request, "ResourceFinderApp/Login.html", {"form": form})


@login_required(login_url='resource_finder/accounts/login')
def PatientHomeView(request):
    if request.user.is_patient:
        patient = Patient.objects.get(user=request.user.id)
        requirement = getattr(patient, "requiements")
        city = getattr(patient, "city")
        facilities_available = Institution.objects.filter(
            type=requirement, city=city)
        return render(request, "ResourceFinderApp/PatientHome.html", {"available": facilities_available, "requirements": requirement})
    else:
        messages.error(request, "Denied: Not a Patient")
        return redirect("login")


@login_required(login_url='resource_finder/accounts/login')
def InstituteHomeView(request):
    if request.user.is_institution:
        return render(request, "ResourceFinderApp/InstituteHome.html")


def LandingPageView(request):
    return render(request, "LandingPage.html")
