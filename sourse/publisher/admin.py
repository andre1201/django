import site
from django.contrib import admin

from django.contrib import admin

from .models import *

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
