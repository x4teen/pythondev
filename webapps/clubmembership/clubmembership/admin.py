from django.contrib import admin
from .models import Person, Group, Fee

admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Fee)
