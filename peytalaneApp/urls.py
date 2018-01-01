from django.conf.urls import url
from peytalaneApp.views.index import index
from peytalaneApp.views.inscription import Inscription
from peytalaneApp.views.login import Login
from peytalaneApp.views.reservation import Reservation

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^inscription/$', Inscription.as_view(), name='inscription'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^reservation/$', Reservation.as_view(), name='reseration'),

]