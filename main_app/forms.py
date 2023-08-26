from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import Checklist, Activities, User, Trips, Destinations, Travelers
from django.contrib.auth.models import User
# for data validation & dropdown menu
from .data.countries import valid_countries

class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['todos', 'complete']
        labels = {
            'todos': '',  # Set the label to an empty string
            'complete': '',  # Set the label to an empty string
        }

class ActivityForm(ModelForm):
    class Meta:
        model = Activities
        fields = ['plannedAct', 'endDate', 'dueDate']

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class TripCreateForm(forms.ModelForm):
    country = forms.ChoiceField(choices=valid_countries)
    class Meta:
        model = Trips
        fields = ['name', 'country', 'startDate', 'endDate', 'budget']

    def clean_country(self):
        country = self.cleaned_data['country']
        if country not in [choice[0] for choice in valid_countries]:
            raise ValidationError("Invalid country name")
        return country
    
class AddDestinationForm(forms.ModelForm):
    country = forms.ChoiceField(choices=valid_countries)
    class Meta:
        model = Destinations
        fields = ['name', 'country', 'language', 'currency']
        widgets = {'destination_ids': forms.CheckboxSelectMultiple} 
        
    def clean_country(self):
        country = self.cleaned_data['country']
        if country not in [choice[0] for choice in valid_countries]:
            raise ValidationError("Invalid country name")
        return country

class InvitationForm(forms.ModelForm):
    class Meta:
        model = Trips # this is the model we're trying to add data to
        fields = ['accepted_users'] # this is the field it's adding to in the Trips model
        widgets = {'accepted_users': forms.CheckboxSelectMultiple}