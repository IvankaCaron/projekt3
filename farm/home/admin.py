from django.contrib import admin
from .models import Friend, Post

# Register your models here.

admin.site.register(Post)
admin.site.register(Friend)