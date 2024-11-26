from django.shortcuts import render
from diet_log.forms import WaterForm, WeightForm, WorkoutForm, MilesForm, LoginForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm

@login_required
def index(request):
    current_date = timezone.now().date()
    context = {
        'water_form': WaterForm(),
        'current_date': current_date,
        'weight_form': WeightForm(),
        'workout_form': WorkoutForm(),
        'miels_form': MilesForm(),
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