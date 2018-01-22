from django.conf.urls import url
from peytalaneApp.views.index import index
from peytalaneApp.views.inscription import Inscription
from peytalaneApp.views.login import Login
from peytalaneApp.views.reservation import Reservation
<<<<<<< HEAD
from peytalaneApp.views.reservation_food import Reservation_food
=======
from peytalaneApp.views.reservation_tournament import Reservation_tournament
>>>>>>> f04fc667f519533bd00ec9ba96d9d2906de84bfd

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^inscription/$', Inscription.as_view(), name='inscription'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^reservation/$', Reservation.as_view(), name='reservation'),
    url(r'^reservation/food/$', Reservation_food.as_view(), name='reservation-food'), 
    url(r'^reservation/tournament/$', Reservation_tournament.as_view(), name='reservation_tournament'),
]
