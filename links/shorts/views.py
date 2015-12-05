from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.utils import timezone
from django.views import generic

from .models import Link

def index(request):
    links = Link.objects.all()
    return render(request, 'short/index.html', {'links' : links})

def short(request, short):
    link = get_object_or_404(Link, short=short)
    link.clicks += 1
    link.last_access_date = timezone.now()
    link.save()
    return render(request, 'short/go.html', {'link': link})

def new(request):
    if 'url' in request.POST:
        link = Link.create(url=request.POST['url'])
        return render(request, 'short/details.html', {'link': link})
    else:
        return render(request, 'short/new.html', {})
