from django.contrib import admin
from .models import articles,qurans_ayats,chapter_ayats

# Register your models here.
admin.site.register(articles)
admin.site.register(chapter_ayats)
admin.site.register(qurans_ayats)

