from django.contrib import admin

# Register your models here.
from .models import Note, User, Type


admin.site.register(Note)
admin.site.register(User)
admin.site.register(Type)

