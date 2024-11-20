from django import forms
from django.utils import timezone

class WaterForm(forms.Form):
    ammount = forms.IntegerField()
    date = forms.DateField(initial=timezone.now().date())


class WeightForm(forms.Form):
    ammount = forms.IntegerField()
    date = forms.DateField(initial=timezone.now().date())

class WeightForm(forms.Form):
    amount = forms.IntegerField()
    date = forms.DateField(initial=timezone.now().date())

class WorkoutForm(forms.Form):
    WORKOUT_CHOICES = [
        (1, 'pilates'),
        (2, 'swimming'),
        (3, 'running'),
        (4, 'walking')
    ]
    
    minutes = forms.IntegerField()
    date = forms.DateField(initial=timezone.now().date())
    name = forms.ChoiceField(choices=WORKOUT_CHOICES)

class MilesForm(forms.Form):
    time = forms.TimeField(
        initial=timezone.now().time(), 
        widget=forms.TimeInput(attrs={'type': 'time'})
    )
    date = forms.DateField(initial=timezone.now().date())
    content = forms.CharField(
        widget=forms.Textarea,
        max_length=200,
        help_text="Maximum 200 characters"
    )

