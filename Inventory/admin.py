from django.contrib import admin
from .models import Computer, Projector, Server, System, Email

# Register your models here.
admin.site.register(Computer)
admin.site.register(Projector)
admin.site.register(Server)
admin.site.register(System)
admin.site.register(Email)