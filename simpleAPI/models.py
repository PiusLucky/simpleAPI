import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .utils import generateUUID
from django.utils import timezone


# just to avoid unnamed constant
MAX_UUID_LENGTH = 33

class UUID(models.Model):
  created = models.DateTimeField(default=timezone.now)
  uuid = models.CharField(
    verbose_name=_('UUID'), default=generateUUID(), 
    max_length= MAX_UUID_LENGTH, blank=False, null=False
  )
  
  
  def __str__(self):
      return str(self.uuid)
      
  class Meta:
      ordering = ["-created"]
