from django.conf.urls import url
from peytalaneApp.views.index import index
from peytalaneApp.views.inscription import Inscription
from peytalaneApp.views.login import Login
from peytalaneApp.views.reservation import Reservation
from peytalaneApp.views.reservation_food import Reservation_food

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^inscription/$', Inscription.as_view(), name='inscription'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^reservation/$', Reservation.as_view(), name='reservation'),
    url(r'^reservation/food/$', Reservation_food.as_view(), name='reservation-food'),  
]
