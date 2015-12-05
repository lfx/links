from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<short>[a-z0-9]+)/$', views.short, name='short'),
    url(r'^new$', views.new, name='new'),
    url(r'^(?P<short>[a-z0-9]+)/d/$', DetailView.as_view(model=Link,
        queryset=Link.objects.filter(short=short)[0]), name='shortdetails'),
]
