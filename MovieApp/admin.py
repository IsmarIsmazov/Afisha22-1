from django.contrib import admin
from MovieApp.models import *
# Register your models here.

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Review)