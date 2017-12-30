from django.conf.urls import url
from peytalaneApp.views.index import index
from peytalaneApp.views.inscription import inscription
from peytalaneApp.views.login import login
from peytalaneApp.views.reservation import reservation

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^inscription/$', inscription.as_view(), name='inscription'),
    url(r'^login/$', login.as_view(), name='login'),
    url(r'^reservation/$', reservation.as_view(), name='reseration'),

]