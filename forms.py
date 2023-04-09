from django import forms
from .models import Note, Beacon, Event

class NoteForm(forms.ModelForm):
    beacon = forms.ModelChoiceField(queryset=Beacon.objects.filter(connected=True), required=False)
    severity = forms.ChoiceField(choices=Note.SEVERITY_CHOICES, widget=forms.RadioSelect, initial='normal')
    class Meta:
        model = Note
        fields = ['beacon', 'content', 'host_ip', 'target_ip', 'severity']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['content']

