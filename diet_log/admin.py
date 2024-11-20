from django.contrib import admin

# Register your models here.
from .models import Water, Wieght, Workout, Miles, FavMiles

admin.site.register(Water)
admin.site.register(Wieght)
admin.site.register(Workout)
admin.site.register(Miles)
admin.site.register(FavMiles)