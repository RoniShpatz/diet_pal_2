from django.shortcuts import render
from diet_log.forms import WaterForm, WeightForm, WorkoutForm, MilesForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

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


def logout_view(request):
    logout(request)
    return redirect('login')
# Create your views here.
