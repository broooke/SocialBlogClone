from django.contrib import admin
from .models import Group, Post, members

# Register your models here.

admin.site.register(Group)
admin.site.register(Post)
admin.site.register(members)

