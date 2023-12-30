from django.contrib import admin

# Register your models here.

from movie.models import Movies

admin.site.register(Movies)