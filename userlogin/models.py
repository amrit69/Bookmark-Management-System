import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Register(models.Model):
    first_name_text = models.CharField(max_length=30)
    last_name_text = models.CharField(max_length=30)
    email_text = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.register_text




