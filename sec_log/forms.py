# sec_log/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import Event

class EventForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Select User")

    class Meta:
        model = Event
        fields = ['user', 'title', 'description']
