from django.shortcuts import render
from diet_log.forms import WaterForm, WeightForm, WorkoutForm, MealsForm, LoginForm, UserUpdateForm, FavMealsForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from .models import Water, Wieght, Workout, Meals, FavMeals
from django.db.models import Sum
from django.utils.timezone import timedelta
from django.shortcuts import get_object_or_404, redirect
from dietBlog.forms import PostForm



@login_required
def index(request):
    if 'current_date' not in request.session:
        request.session['current_date'] = timezone.now().date().strftime('%Y-%m-%d')
    current_date = timezone.datetime.strptime(request.session['current_date'], '%Y-%m-%d').date()

    # Fetch existing data for the logged-in user
    water_entries = Water.objects.filter(user_id=request.user, date=current_date)
    total_water = water_entries.aggregate(Sum('mil'))['mil__sum'] or 0

    weight =  Wieght.objects.filter(user_id=request.user, date=current_date)
    workout = Workout.objects.filter(user_id=request.user, date=current_date)

    fav_meal_list =FavMeals.objects.filter(user_id=request.user).order_by('name')


    meals_entries = Meals.objects.filter(user_id=request.user, date=current_date).order_by('time')

    context = {
        'water_total': total_water,
        'weight': weight,
        'workout': workout,
        'meals_entries': meals_entries,
        'water_form': WaterForm(),
        'current_date': current_date,
        'weight_form': WeightForm(),
        'workout_form': WorkoutForm(),
        'meals_form': MealsForm(),
        'post_form': PostForm(),
        'fav_meal': fav_meal_list,
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
                water_entry.date = water_form.cleaned_data['date']
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
                weight_entry.date = weight_form.cleaned_data['date']
                weight_entry.save()
                messages.success(request, 'Weight entry added successfully!')
                return redirect('index')
        elif 'update_weight' in request.POST:
            weight_id = request.POST.get('weight_id')
            weight_entry = get_object_or_404(Wieght, id=weight_id, user_id=request.user)
            weight_form = WeightForm(request.POST, instance=weight_entry)
            if weight_form.is_valid():
                weight_form.save()
                messages.success(request, 'Weight entry updated successfully!')
            else:
                messages.error(request, 'Failed to update weight entry.')
        elif 'delete_weight' in request.POST:
            weight_id = request.POST.get('weight_id')
            weight_entry = get_object_or_404(Wieght, id=weight_id, user_id=request.user)
            weight_form = WeightForm(request.POST, instance=weight_entry)
            if weight_form.is_valid():
                weight_entry.delete()
                messages.success(request, 'Weight entry deleted successfully!')
        # Workout Form Handling
        elif 'submit_workout' in request.POST:
            workout_form = WorkoutForm(request.POST)
            if workout_form.is_valid():
                workout_entry = workout_form.save(commit=False)
                workout_entry.user_id = request.user
                workout_entry.date = workout_form.cleaned_data['date']
                workout_entry.save()
                messages.success(request, 'Workout entry added successfully!')
                return redirect('index')
        elif 'update_workout' in request.POST:
            workout_id = request.POST.get('workout_id')
            workout_entry = get_object_or_404(Workout, id=workout_id, user_id=request.user)
            workout_form = WorkoutForm(request.POST, instance=workout_entry)
            if workout_form.is_valid():
                workout_form.save()
                messages.success(request, 'Workout entry updated successfully!')
            else:
                messages.error(request, 'Failed to update workout entry.')
        elif 'delete_workout' in request.POST:
            workout_id  = request.POST.get('workout_id')
            workout_entry = get_object_or_404(Workout, id=workout_id, user_id=request.user)
            workout_form = WorkoutForm(request.POST, instance=workout_entry)
            if workout_form.is_valid():
                workout_entry.delete()
                messages.success(request, 'Workout entry deleted successfully!')       
        # Meals Form Handling
        elif 'submit_meal' in request.POST:
            meals_form = MealsForm(request.POST)
            if meals_form.is_valid():
                meals_entry = meals_form.save(commit=False)
                meals_entry.user_id = request.user
                meals_entry.date = meals_form.cleaned_data['date']
                meals_entry.save()
                messages.success(request, 'Meal entry added successfully!')
                return redirect('index')
        elif 'update_meal' in request.POST:
            meal_id = request.POST.get('meal_id')
            meals_entry =  get_object_or_404(Meals, id=meal_id, user_id=request.user)
            meals_form = MealsForm(request.POST, instance=meals_entry)
            if meals_form.is_valid():
                meals_form.save()
                messages.success(request, 'Meal entry updated successfully!')
            else:
                messages.error(request, 'Failed to update meal entry.') 
        elif 'delete_meal' in request.POST:
            meal_id = request.POST.get('meal_id')
            meals_entry =  get_object_or_404(Meals, id=meal_id, user_id=request.user)
            meals_form = MealsForm(request.POST, instance=meals_entry)
            if meals_form.is_valid():
                meals_entry.delete()
                messages.success(request, 'Meal entry deleted successfully!')     
        # date display info
        elif 'prev_date' in request.POST:
            current_date -= timedelta(days=1)
            request.session['current_date'] = current_date.strftime('%Y-%m-%d')
            return redirect('index')
        elif 'next_date' in request.POST:
            current_date += timedelta(days=1)
            request.session['current_date'] = current_date.strftime('%Y-%m-%d')
            return redirect('index')
        #share water data in blog
        elif 'share-water' in request.POST:
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                post_entry = post_form.save(commit=False)
                post_entry.author_id = request.user.id
                post_entry.title = post_form.cleaned_data['title'] 
                post_entry.content = post_form.cleaned_data['content']
                post_entry.save()
                return redirect('dietBlog:post_list')
            else:
                messages.error(request, "Failed to share water intake.")
        #share weight data in blog
        elif 'share-weight' in request.POST:
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                post_entry = post_form.save(commit=False)
                post_entry.author_id = request.user.id
                post_entry.title = post_form.cleaned_data['title'] 
                post_entry.content = post_form.cleaned_data['content']
                post_entry.save()
                return redirect('dietBlog:post_list')
            else:
                messages.error(request, "Failed to share weight intake.")
        #share workout data in blog
        elif 'share-workout' in request.POST:
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                post_entry = post_form.save(commit=False)
                post_entry.author_id = request.user.id
                post_entry.title = post_form.cleaned_data['title'] 
                post_entry.content = post_form.cleaned_data['content']
                post_entry.save()
                return redirect('dietBlog:post_list')
            else:
                messages.error(request, "Failed to share workout intake.")      
        #share meal data in blog
        elif 'share-meal' in request.POST:
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                post_entry = post_form.save(commit=False)
                post_entry.author_id = request.user.id
                post_entry.title = post_form.cleaned_data['title'] 
                post_entry.content = post_form.cleaned_data['content']
                post_entry.save()
                return redirect('dietBlog:post_list')
            else:
                messages.error(request, "Failed to share meal intake.")  

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


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile') 
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'profile.html', {'form': form})


@login_required
def fav_meal(request):
    fav_meal_list = FavMeals.objects.filter(user_id=request.user).order_by('name')
    fav_meal_form = FavMealsForm()
    
    if request.method == 'POST':
        if 'submit-fav-meal' in request.POST:
            fav_meal_form = FavMealsForm(request.POST)
            if fav_meal_form.is_valid():
                fav_entry = fav_meal_form.save(commit=False)
                fav_entry.user_id = request.user
                fav_entry.save()
                messages.success(request, 'Fav meal entry added successfully!')
                return redirect('fav_meal')
            else:
                print("Fav Meal Form Errors:", fav_meal_form.errors)
        elif 'updtae-fav-meal' in request.POST:
            fav_meal_id = request.POST.get('fav_meal_id')
            fav_entry = get_object_or_404(FavMeals, id=fav_meal_id, user_id=request.user)
            fav_meal_form = FavMealsForm(request.POST, instance=fav_entry)
            if fav_meal_form.is_valid():
                fav_meal_form.save()
                messages.success(request, 'Fav Meal entry updated successfully!')
                return redirect('fav_meal')
            else:
                messages.error(request, 'Failed to update fav meal entry.') 
        elif 'delete-fav-meal' in request.POST:
            fav_meal_id = request.POST.get('fav_meal_id')
            fav_entry = get_object_or_404(FavMeals, id=fav_meal_id, user_id=request.user)
            fav_meal_form = FavMealsForm(request.POST, instance=fav_entry)
            if fav_meal_form.is_valid():
                fav_entry.delete()
                messages.success(request, 'Fav Meal entry deleted successfully!')
                return redirect('fav_meal')
            else:
                messages.error(request, 'Failed to delete fav meal entry.') 
    return render(request, 'fav_meal.html', {
        'fav_meal': fav_meal_list, 
        'fav_meal_form': fav_meal_form
    })




