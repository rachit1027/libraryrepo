from django.contrib import admin
from .models import Book

# Register your models here.

admin.site.register([Book])

# superuser name and pass are "hello"
