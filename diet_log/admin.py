from django.contrib import admin

# Register your models here.
from .models import Water, Wieght, Workout, Meals, FavMeals

admin.site.register(Water)
admin.site.register(Wieght)
admin.site.register(Workout)
admin.site.register(Meals)
admin.site.register(FavMeals)