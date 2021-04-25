from os import name
from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/patient-sign-up', PatientSignUpView, name="patient-sign-up"),
    path('accounts/institute-sign-up',
         InstituteSignUpView, name="institute-sign-up"),
    path('accounts/login', LoginView, name="login"),
    path('patient_home/', PatientHomeView, name="patient_home"),
    path('institute_home/', InstituteHomeView, name="institute_home"),
    path('welcome_page/', LandingPageView, name="welcome_page"),
]
