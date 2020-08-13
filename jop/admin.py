from django.contrib import admin

# Register your models here.

from .models import Jop , Category , Applyer
admin.site.register(Jop)

admin.site.register(Category)

admin.site.register(Applyer)