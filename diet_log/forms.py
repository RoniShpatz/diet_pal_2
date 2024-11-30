from django import forms
from django.utils import timezone
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Meals, Water, Wieght, Workout, FavMeals

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

class WaterForm(forms.ModelForm):
    class Meta:
        model = Water  
        fields = ['mil', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = timezone.now().date()

class WeightForm(forms.ModelForm):
    class Meta:
        model = Wieght 
        fields = ['amount', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = timezone.now().date()

WORKOUT_CHOICES = [
        ('pilates','pilates'),
        ('swimming', 'swimming'),
        ('running', 'running'),
        ('walking', 'walking')
    ]

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout  # Assuming you have a Workout model
        fields = ['name', 'duration', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'duration': forms.NumberInput(attrs={
                'type': 'number',
                'min': '0',  
                'step': '1'   
            }),
            'name': forms.Select(choices=WORKOUT_CHOICES)
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = timezone.now().date()

class MealsForm(forms.ModelForm):
    class Meta:
        model = Meals  # Assuming you have a Meals model
        fields = ['content', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'content': forms.Textarea(attrs={'rows': 3, 'max_length': 200})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = timezone.now().date()
        self.fields['time'].initial = timezone.now().time()
        self.fields['content'].help_text = "Maximum 200 characters"

