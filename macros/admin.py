from django.contrib import admin
from .models import Step, Ingredient, Recipe, UserGoal

# Register your models here.
admin.site.register([Step, Ingredient, Recipe, UserGoal])
