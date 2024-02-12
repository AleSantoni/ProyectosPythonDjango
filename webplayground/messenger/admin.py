
from django.contrib import admin
from .models import Thread, Message

# Registra los modelos en el admin
admin.site.register(Thread)
admin.site.register(Message)