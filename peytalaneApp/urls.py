from django.conf.urls import url
from peytalaneApp.views.index import index
from peytalaneApp.views.pay import Pay
from peytalaneApp.views.inscription import Inscription
from peytalaneApp.views.login import Login
from peytalaneApp.views.reservation import Reservation
from peytalaneApp.views.reservation_food import Reservation_food
from peytalaneApp.views.reservation_tournament import Reservation_tournament
from peytalaneApp.views.admin import *
from django.contrib.auth.views import logout



urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^inscription/$', Inscription.as_view(), name='inscription'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^reservation/$', Reservation.as_view(), name='reservation'),
    url(r'^reservation/food/$', Reservation_food.as_view(), name='reservation-food'),
    url(r'^reservation/tournament/$', Reservation_tournament.as_view(), name='reservation_tournament'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^pay/$', Pay.as_view(), name='pay'),
    url(r'^reservation/admin/food', Food_admin.as_view(), name='food_admin'),
    url(r'^reservation/admin/user', User_admin.as_view(), name='user_admin'),

    #url(r'^user/admin', User_admin.as_view(), name='user_admin'),
    #url(r'^reservation/admin/user', User_admin.as_view(), name='user_admin'),
    #url(r'^reservation/admin/user', User_admin.as_view(), name='user_admin'),

    #url(r'^reservation/food/search', Reservation_food_search, name='')
]
