from django.contrib import admin
from .models import Movie, Rating
# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass