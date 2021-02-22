from django.db import models

# Create your models here.
from django.contrib import admin
class Participant(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    place=models.CharField(max_length=50)

class ParticipantAdmin(admin.ModelAdmin):
    list_display=("name","email","phone","place")