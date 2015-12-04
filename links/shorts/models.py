import datetime
from django.db import models
from django.utils import timezone

class Link(models.Model):
   url = models.CharField(max_length=2000)
   short = models.CharField(max_length=10, db_index=True)
   pub_date = models.DateTimeField('date published', auto_now_add=True, db_index=True)
   last_access_date = models.DateTimeField('last accessed', auto_now_add=True, db_index=True)
   clicks = models.IntegerField(default=0)

   def was_published_recently(self):
       return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

   def __str__(self):
       return self.url + " (" + str(self.clicks) + ")";

   @classmethod
   def create(cls, url):
       shortlistSet = ShortList.objects.filter(in_use=False)[:1]
       for shortlist in shortlistSet:
           short_url = shortlist.short
           shortlist.in_use = True
           shortlist.save()

       link = cls(url=url, short=short_url, pub_date = timezone.now())
       link.save()
       return link

class ShortList(models.Model):
    short = models.CharField(max_length=10)
    in_use = models.BooleanField(default=False)
