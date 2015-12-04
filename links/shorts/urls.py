from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<short>[a-z0-9]+)/$', views.short, name='short'),
    url(r'^new$', views.new, name='new'),
    url(r'^(?P<short>[a-z0-9]+)/d/$', views.shortdetails, name='shortdetails'),

]
