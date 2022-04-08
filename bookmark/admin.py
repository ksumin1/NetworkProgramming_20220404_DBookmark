from django.contrib import admin

# Register your models here.
from bookmark.models import Bookmark

admin.site.register(Bookmark)