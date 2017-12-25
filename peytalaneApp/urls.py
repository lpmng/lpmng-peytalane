from django.conf.urls import url
from peytalaneApp.views.index import index
from peytalaneApp.views.inscription import inscription

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^inscription/$', inscription, name='inscription'),
]