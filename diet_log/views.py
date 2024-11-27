from django.shortcuts import render
from diet_log.forms import WaterForm, WeightForm, WorkoutForm, MealsForm, LoginForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages

@login_required
def index(request):
    current_date = timezone.now().date()
    context = {
        'water_form': WaterForm(),
        'current_date': current_date,
        'weight_form': WeightForm(),
        'workout_form': WorkoutForm(),
        'meals_form': MealsForm(),
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to home page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def view(request):
    current_date = timezone.now().date()
    
    if request.method == 'POST':
        # Check which form was submitted
        if 'submit_water' in request.POST:
            water_form = WaterForm(request.POST)
            if water_form.is_valid():
                water_entry = water_form.save(commit=False)
                water_entry.user = request.user  # Assuming you're using user authentication
                water_entry.save()
                messages.success(request, 'Water entry added successfully!')
                return redirect('your_view_name')
            water_form = WaterForm()
        else:
            water_form = WaterForm()
        
        if 'submit_weight' in request.POST:
            weight_form = WeightForm(request.POST)
            if weight_form.is_valid():
                weight_entry = weight_form.save(commit=False)
                weight_entry.user = request.user
                weight_entry.save()
                messages.success(request, 'Weight entry added successfully!')
                return redirect('your_view_name')
            weight_form = WeightForm()
        else:
            weight_form = WeightForm()
        
        # Similar blocks for workout and miles forms
        if 'submit_workout' in request.POST:
            workout_form = WorkoutForm(request.POST)
            if workout_form.is_valid():
                workout_entry = workout_form.save(commit=False)
                workout_entry.user = request.user
                workout_entry.save()
                messages.success(request, 'Workout entry added successfully!')
                return redirect('your_view_name')
            workout_form = WorkoutForm()
        else:
            workout_form = WorkoutForm()
        
        if 'submit_meal' in request.POST:
            miles_form = MealsForm(request.POST)
            if miles_form.is_valid():
                miles_entry = miles_form.save(commit=False)
                miles_entry.user = request.user
                miles_entry.save()
                messages.success(request, 'Miles entry added successfully!')
                return redirect('your_view_name')
            miles_form = MealsForm()
        else:
            miles_form = MealsForm()
    
    else:

        water_form = WaterForm()
        weight_form = WeightForm()
        workout_form = WorkoutForm()
        miles_form = MealsForm()
    
    context = {
        'water_form': water_form,
        'current_date': current_date,
        'weight_form': weight_form,
        'workout_form': workout_form,
        'meals_form': miles_form,
    }
    
    return render(request, 'index.html', context)