from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_institution = models.BooleanField(default=False)


class Patient(models.Model):
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
        ('BED', 'Normal Hospital Bed'),
        ('REM', 'Remdesivir'),
        ('CLN', 'Clinic')
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
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    patient_name = models.CharField(
        verbose_name="Patient Name", max_length=250)
    city = models.CharField(choices=CITIES, default='MUM',
                            max_length=3, verbose_name='City Name')
    phone = PhoneNumberField()
    email = models.EmailField(verbose_name="email id", max_length=254)
    results = models.CharField(
        verbose_name='COVID Test Results', max_length=2, default='D')
    oxygen_level = models.IntegerField(verbose_name='Oxygen Level', validators=[
                                       MinValueValidator(0), MaxValueValidator(100)])
    requiements = models.CharField(
        verbose_name='Requirements', choices=REQUIREMENTS, max_length=3)
    morbidities = models.CharField(
        verbose_name='Other Complications', choices=OTHER_COMPLICATIONS, max_length=1)
    vaccination_does = models.IntegerField(choices=DOSES, default=0)
    timestamp = models.DateTimeField(auto_now=True)


class Institution(models.Model):
    CITIES = (
        ('MUM', 'Mumbai'),
        ('PNQ', 'Pune'),
        ('BLR', 'Bnaglore'),
        ('DEL', 'Delhi'),
        ('KOL', 'Kolkata'),
    )
    TYPE = (
        ('O2', 'Oxygen'),
        ('ICU', 'ICU'),
        ('BED', 'Normal Hospital Bed'),
        ('REM', 'Remdesivir'),
        ('CLN', 'Clinic')
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    institute_name = models.CharField(
        verbose_name="Institution Name", max_length=250)
    city = models.CharField(choices=CITIES, default='MUM',
                            max_length=3, verbose_name='City Name')
    phone = PhoneNumberField()
    email = models.EmailField(verbose_name="email id", max_length=254)
    type_institute = models.CharField(choices=TYPE, max_length=3,
                                      verbose_name='Type of Facility', default='BED')
    available = models.IntegerField(
        verbose_name='Number of utilities avaialable')


class PatientFiles(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    id_proof = models.FileField(
        verbose_name="ID Proof", upload_to='identification/')
    covid_report = models.FileField(
        verbose_name="COVID Report", upload_to='covid_report/')
    oxymeter_img = models.ImageField(
        verbose_name="Oxygen Level Proof", upload_to='oxygen/')
    other_reports = models.FileField(
        verbose_name="Other Reports", upload_to='reports/')


class Application(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    institute = models.ForeignKey(Institution, on_delete=models.CASCADE)
