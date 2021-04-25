from django import VERSION, forms
from django.db.models import fields
from django.forms import ModelForm, Form
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, Institution, User, PatientFiles
from django.db import models, transaction
from phonenumber_field.formfields import PhoneNumberField


class PatientSignUpForm(UserCreationForm):
    CITIES = (
        ('MUM', 'Mumbai'),
        ('PNQ', 'Pune'),
        ('BLR', 'Bnaglore'),
        ('DEL', 'Delhi'),
        ('KOL', 'Kolkata'),
    )
    COVID_RESULTS = (
        ('NA', 'Not Applicable'),
        ('D', 'Detected'),
        ('ND', 'Not Detected'),
    )
    REQUIREMENTS = (
        ('O2', 'Oxygen'),
        ('ICU', 'ICU'),
        ('BED', 'Normal Bed'),
        ('REM', 'Remdesivir'),
    )
    OTHER_COMPLICATIONS = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    DOSES = (
        (0, 'Not Taken'),
        (1, 'Once'),
        (2, 'Twice')
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "password1", "password2", "email"]

    patient_name = forms.CharField()
    city = forms.CharField()
    phone = PhoneNumberField()
    results = forms.ChoiceField(choices=COVID_RESULTS)
    oxygen_level = forms.IntegerField()
    requiements = forms.ChoiceField(choices=REQUIREMENTS)
    morbidities = forms.ChoiceField(choices=OTHER_COMPLICATIONS)
    vaccination_does = forms.ChoiceField(choices=DOSES)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient = Patient.objects.create(user=user)
        patient.patient_name = self.cleaned_data.get("patient_name")
        patient.city = self.cleaned_data.get("city")
        patient.phone = self.cleaned_data.get("phone")
        patient.results = self.cleaned_data.get("results")
        patient.oxygen_level = self.cleaned_data.get("oxygen_level")
        patient.requirements = self.cleaned_data.get("requirements")
        patient.morbidities = self.cleaned_data.get("morbidities")
        patient.vaccination_doses = self.cleaned_data.get("vaccination_doses")
        patient.save()
        return user


class InstituteSignUpForm(UserCreationForm):
    CITIES = (
        ('MUM', 'Mumbai'),
        ('PNQ', 'Pune'),
        ('BLR', 'Bnaglore'),
        ('DEL', 'Delhi'),
        ('KOL', 'Kolkata'),
    )
    TYPE = (
        ('H', 'Hospital'),
        ('C', 'Clinic'),
        ('O', 'Oxygen Supplier'),
        ('I', 'Hospital with ICU'),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "password1", "password2", "email"]

    institution_name = forms.CharField()
    city = forms.ChoiceField(choices=CITIES)
    phone = PhoneNumberField()
    waitlist = forms.IntegerField()
    type_institute = forms.ChoiceField(choices=TYPE)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_institution = True
        user.save()
        institute = Institution.objects.create(user=user)
        institute.institution_name = self.cleaned_data.get("institution_name")
        institute.city = self.cleaned_data.get("city")
        institute.phone = self.cleaned_data.get("phone")
        institute.type_institute = self.cleaned_data.get("type_institute")
        institute.waitlist = self.cleaned_data.get("waitlist")
        institute.save()
        return user


class PatientFurtherDetailsForm(ModelForm):
    class Meta:
        model = PatientFiles
        exclude = ['patient']
