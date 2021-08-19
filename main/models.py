from django.db import models
from django.urls import reverse

class NotePad(models.Model):
    title = models.CharField(max_length=200, unique_for_date=True)
    description = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("note_detail", kwargs={"title": self.title,
                                              'day':self.date_created.day,
                                              'month':self.date_created.month,
                                              'year':self.date_created.year
                                              })
    