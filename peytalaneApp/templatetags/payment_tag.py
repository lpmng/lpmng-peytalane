from django import template
from peytalaneApp.models_dir.payment import *


register = template.Library()

def get_value_option(payment, arg):
    try:
        return Payment_option_value.objects.get(option=arg,payment=payment).value
    except Payment_option_value.DoesNotExist:
        return "non"

register.filter('get_value_option', get_value_option)