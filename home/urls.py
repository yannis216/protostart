from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^impressum/$', views.impressum, name='impressum'),
]
