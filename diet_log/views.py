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
from .models import Water, Wieght, Workout, Meals


@login_required
def index(request):
    current_date = timezone.now().date()

    
    # Fetch existing data for the logged-in user
    water_entries = Water.objects.filter(user_id=request.user).order_by('-date')
    weight_entries =  Wieght.objects.filter(user_id=request.user).order_by('-date')
    workout_entries = Workout.objects.filter(user_id=request.user).order_by('-date')
    meals_entries = Meals.objects.filter(user_id=request.user).order_by('-date')

    context = {
        'current_date': current_date,
        'water_entries': water_entries,
        'weight_entries': weight_entries,
        'workout_entries': workout_entries,
        'meals_entries': meals_entries,
        'water_form': WaterForm(),
        'current_date': current_date,
        'weight_form': WeightForm(),
        'workout_form': WorkoutForm(),
        'meals_form': MealsForm(),
    }

    # Initialize forms for GET requests or invalid POST submissions
    water_form = WaterForm()
    weight_form = WeightForm()
    workout_form = WorkoutForm()
    meals_form = MealsForm()

    if request.method == 'POST':
        # Water Form Handling
        if 'submit_water' in request.POST:
            water_form = WaterForm(request.POST)
            if water_form.is_valid():
                water_entry = water_form.save(commit=False)
                water_entry.user_id = request.user
                water_entry.save()
                messages.success(request, 'Water entry added successfully!')
                return redirect('index')
            else:
                print("Water Form Errors:", water_form.errors)

        # Weight Form Handling
        elif 'submit_weight' in request.POST:
            weight_form = WeightForm(request.POST)
            if weight_form.is_valid():
                weight_entry = weight_form.save(commit=False)
                weight_entry.user_id = request.user
                weight_entry.save()
                messages.success(request, 'Weight entry added successfully!')
                return redirect('index')

        # Workout Form Handling
        elif 'submit_workout' in request.POST:
            workout_form = WorkoutForm(request.POST)
            if workout_form.is_valid():
                workout_entry = workout_form.save(commit=False)
                workout_entry.user_id = request.user
                workout_entry.save()
                messages.success(request, 'Workout entry added successfully!')
                return redirect('index')

        # Meals Form Handling
        elif 'submit_meal' in request.POST:
            meals_form = MealsForm(request.POST)
            if meals_form.is_valid():
                meals_entry = meals_form.save(commit=False)
                meals_entry.user_id = request.user
                meals_entry.save()
                messages.success(request, 'Meal entry added successfully!')
                return redirect('index')
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

