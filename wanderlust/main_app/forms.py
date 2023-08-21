from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Checklist, Activities, User

class ChecklistForm(ModelForm):
  class Meta:
    model = Checklist
    fields = ['todos', 'complete']

class ActivityForm(ModelForm):
    class Meta:
        model = Activities
        fields = ['plannedAct', 'endDate', 'dueDate']

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']