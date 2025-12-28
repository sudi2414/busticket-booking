from django import forms
from .models import Bus_Booking   

class Bus_Form(forms.ModelForm):
    class Meta:
        model = Bus_Booking
        exclude = ['bus_number']
        widgets = {'journey_date':forms.DateInput(attrs={'type':'date'})}
