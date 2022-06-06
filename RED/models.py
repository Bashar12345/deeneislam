from django.db import models
import json

# Create your models here.
class articles(models.Model):
    title = models.CharField(max_length=220)
    content = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title

class qurans_ayats(models.Model):
    chapter_id = models.IntegerField(max_length=2,blank=False,null=False)
    chapter_name = models.CharField(max_length=32)
    ayats = models.JSONField(default=dict) # for list of ayats 

