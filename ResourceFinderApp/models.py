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
        ('BED', 'Normal Bed'),
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
    email = models.EmailField(max_length=254, verbose_name='e-mail id')
    results = models.CharField(
        verbose_name='COVID Test Results', max_length=2, default='D')
    oxygen_level = models.IntegerField(verbose_name='Oxygen Level', validators=[
                                       MinValueValidator(0), MaxValueValidator(100)])
    requiements = models.CharField(
        verbose_name='Requirements', choices=REQUIREMENTS, max_length=3)
    morbidities = models.CharField(
        verbose_name='Other Complications', choices=OTHER_COMPLICATIONS, max_length=1)
    vaccination_does = models.IntegerField(choices=DOSES, default=0)


class Institution(models.Model):
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
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    institute_name = models.CharField(
        verbose_name="Institution Name", max_length=250)
    city = models.CharField(choices=CITIES, default='MUM',
                            max_length=3, verbose_name='City Name')
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254, verbose_name='e-mail id')
    type = models.CharField(choices=TYPE, max_length=1,
                            verbose_name='Type of Facility', default='H')
    waitlist = models.IntegerField(verbose_name='People in Waiting')
