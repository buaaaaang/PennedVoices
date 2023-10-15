from django.contrib import admin
from .models import Visualizer
from .models import Minter

# Register your models here.

admin.site.register(Visualizer)
admin.site.register(Minter)