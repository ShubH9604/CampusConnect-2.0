from django import forms
from .models import Event

# Event creation form
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_datetime', 'location', 'photo', 'organized_by']
        widgets = {
            'event_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

# Event registration form
class EventRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    additional_info = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=False)

