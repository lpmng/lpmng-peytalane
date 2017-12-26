from django.conf.urls import url
from peytalaneApp.views.index import index
from peytalaneApp.views.inscription import inscription
from peytalaneApp.views.login import login
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^inscription/$', inscription, name='inscription'),
    url(r'^login/$', login.as_view(), name='login'),
]