from django.contrib import admin
from peytalaneApp.models_dir.user import User
from peytalaneApp.models_dir.food import *
import django

# -- -- -- -- -- -- -- food -- -- -- -- -- -- -- --

class ValueOptionAdmin(admin.ModelAdmin):
    list_display = ('value',)    

class OptionAdmin(admin.ModelAdmin):
    list_display = ('name',)

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')

admin.site.register(ValueOption, ValueOptionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Food, FoodAdmin)

# -- -- -- -- -- -- -- user -- -- -- -- -- -- -- --
