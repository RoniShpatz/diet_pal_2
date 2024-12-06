from django import forms
from django.utils import timezone
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Meals, Water, Wieght, Workout, FavMeals, UploadedFile
from PIL import Image, ImageDraw
import io
from django.core.files.uploadedfile import InMemoryUploadedFile

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
        fields = ['content', 'date', 'time', 'file']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'content': forms.Textarea(attrs={'rows': 3, 'max_length': 200}),
            'file': forms.FileInput(attrs={'accept': 'image/*'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = timezone.now().date()
        current_time = timezone.now().time().strftime('%H:%M')
        self.fields['time'].initial = current_time
        self.fields['content'].help_text = "Maximum 200 characters"


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']  
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists() and self.instance.email != email:
            raise forms.ValidationError("This email is already in use.")
        return email
    

class FavMealsForm(forms.ModelForm):
    class Meta:
        model = FavMeals
        fields = ['name', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'max_length': 20}),
            'content': forms.Textarea(attrs={'rows': 3, 'max_length': 200})
        }
    
class UploadForm(forms.ModelForm):
    file = forms.ImageField(
        required=True,
        widget=forms.FileInput(attrs={'accept': 'image/*'})
    )
    class Meta:
        model = UploadedFile
        fields = ['file']

    def clean_file(self):
        # Add extra validation and debugging
        file = self.cleaned_data.get('file')
        
        # # Debug prints
        # print("File received:", file)
        # print("File type:", type(file))
        
        if not file:
            print("No file found in cleaned_data")
            raise forms.ValidationError("No file was uploaded.")
        
        # Additional checks if needed
        if file.size > 5 * 1024 * 1024:  # 5MB limit
            raise forms.ValidationError("File size must be under 5MB.")
        
        return file

    def save(self, commit=True):
        print("Saving form with commit:", commit)
        instance = super().save(commit=False)

        uploaded_file = self.cleaned_data.get('file')
        processed_file = self.resize_and_crop_image(uploaded_file)
        
        instance.file = processed_file

        if commit:
            # print("Attempting to save instance")
            instance.save()
        
        return instance
    #  Resize and crop an uploaded image to a circular shape
    def resize_and_crop_image(self, uploaded_file, target_size=(200, 200)):
        img = Image.open(uploaded_file)
        
        if img.mode != 'RGB':
            img = img.convert('RGB')

        img.thumbnail(target_size, Image.LANCZOS)
        mask = Image.new('L', img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, img.width, img.height), fill=255)

        # Apply the mask
        output = Image.new('RGBA', img.size, (0, 0, 0, 0))
        output.paste(img, (0, 0), mask)

        # Save to a bytes buffer
        buffer = io.BytesIO()
        output.save(buffer, format='PNG')
        buffer.seek(0)

        # Convert to Django InMemoryUploadedFile
        return InMemoryUploadedFile(
            buffer,
            None,
            f'{uploaded_file.name.split(".")[0]}_circular.png',
            'image/png',
            buffer.getbuffer().nbytes,
            None
        )


class UploadFormMeal(forms.ModelForm):
    file = forms.ImageField(
        required=True,
        widget=forms.FileInput(attrs={'accept': 'image/*'})
    )

    class Meta:
        model = UploadedFile
        fields = ['file']

    def clean_file(self):
        # Add extra validation
        file = self.cleaned_data.get('file')
        
        if not file:
            raise forms.ValidationError("No file was uploaded.")
        
        # Check file size
        if file.size > 5 * 1024 * 1024:  # 5MB limit
            raise forms.ValidationError("File size must be under 5MB.")
        
        return file

    def save(self, commit=True):
        instance = super().save(commit=False)

        uploaded_file = self.cleaned_data.get('file')
        processed_file = self.resize_image(uploaded_file)  # Resize the image
        
        instance.file = processed_file

        if commit:
            instance.save()
        
        return instance

    # Resize the image to exactly 200x200 pixels
    def resize_image(self, uploaded_file, target_size=(200, 200)):
        img = Image.open(uploaded_file)
        
        if img.mode != 'RGB':
            img = img.convert('RGB')  # Ensure the image is in RGB mode

        # Resize the image to the target size
        img = img.resize(target_size, Image.ANTIALIAS)

        # Save to a bytes buffer
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)

        # Convert to Django InMemoryUploadedFile
        return InMemoryUploadedFile(
            buffer,
            None,
            f'{uploaded_file.name.split(".")[0]}_resized.png',
            'image/png',
            buffer.getbuffer().nbytes,
            None
        )