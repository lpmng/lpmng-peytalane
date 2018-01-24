from django.contrib import admin
from peytalaneApp.models_dir.user import User
from peytalaneApp.models_dir.food import *
from peytalaneApp.models_dir.tournament import *
import django

# -- -- -- -- -- -- -- food -- -- -- -- -- -- -- --

class ValueOptionAdmin(admin.ModelAdmin):
    list_display = ('value',)    

class OptionAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ValueIngredientAdmin(admin.ModelAdmin):
    list_display = ('value',)    
    
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')

admin.site.register(ValueOption, ValueOptionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(ValueIngredient, ValueIngredientAdmin)
admin.site.register(Food, FoodAdmin)

# -- -- -- -- -- -- -- user -- -- -- -- -- -- -- --
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)

admin.site.register(User, UserAdmin)

# -- -- -- -- -- -- Tournament -- -- -- -- -- -- --

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name','number_participants','img')

admin.site.register(Tournament, TournamentAdmin)
