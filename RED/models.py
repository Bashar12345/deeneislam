from django.db import models
import json

# Create your models here.
class articles(models.Model):
    title = models.CharField(max_length=220)
    content = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title

class chapter_ayats(models.Model):
    chapter_id = models.IntegerField(blank=False,null=False)
    chapter_name = models.CharField(max_length=100)
    #ayats = models.JSONField(default=dict) # for list of ayats 

class qurans_ayats(models.Model):
    chapter_id = models.ForeignKey(chapter_ayats, on_delete=models.CASCADE)  # mField(blank=False,null=False)
    sura_no = models.IntegerField(blank=False,null=False)
    surah_name = models.CharField(max_length=24)
    ayat_no = models.IntegerField(blank=False) 