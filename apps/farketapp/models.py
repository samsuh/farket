from __future__ import unicode_literals

from django.db import models
#bring in User model from loginapp
from ..loginapp.models import User

# Create your models here.
class Fark(models.Model):
    marketname = models.CharField(max_length=100)
    fmid = models.CharField(max_length=10)
    fark_visitor = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Review(models.Model):
    marketid = models.ForeignKey(Fark)
    commentor = models.ForeignKey(User)
    comment = models.TextField(max_length=1000)
    rating = models.CharField(max_length=3)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
