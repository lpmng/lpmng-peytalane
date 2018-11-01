from django.contrib import admin
from django.contrib.auth.models import Group
from peytalaneApp.models_dir.user import User
from peytalaneApp.models_dir.food import *
from peytalaneApp.models_dir.tournament import *
from peytalaneApp.models_dir.payment import *
import django

# -- -- -- -- -- -- -- food -- -- -- -- -- -- -- --

class ValueOptionAdmin(admin.ModelAdmin):
    list_display = ('value',)    

class OptionAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ValueIngredientAdmin(admin.ModelAdmin):
    list_display = ('value',)    
    
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(ValueOption, ValueOptionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(ValueIngredient, ValueIngredientAdmin)
admin.site.register(Food, FoodAdmin)

'''
# -- -- -- -- -- --  Payment  -- -- -- -- -- -- --

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('type_product','product','price','user')

class OptionPaymentAdmin(admin.ModelAdmin):
    list_display = ('name','value')


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Payment_option, OptionPaymentAdmin)
'''

# -- -- -- -- -- -- -- user -- -- -- -- -- -- -- --
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)

admin.site.register(User, UserAdmin)

# -- -- -- -- -- -- Tournament -- -- -- -- -- -- --

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name','number_participants','img')


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('user','game_pseudo')


admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.unregister(Group)