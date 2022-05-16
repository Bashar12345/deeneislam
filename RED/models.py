from django.db import models

# Create your models here.
class articles(models.Model):
    title = models.CharField(max_length=220)
    content = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title