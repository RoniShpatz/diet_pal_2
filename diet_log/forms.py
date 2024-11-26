from django import forms
from django.utils import timezone
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            Submit('submit', 'Login', css_class='btn btn-primary')
        )

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

