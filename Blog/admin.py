from django.contrib import admin
from .models import *


# Register your models here.
def register(model):
    admin.site.register(model)

register(BlogPost)
register(Comment)
register(Projects)