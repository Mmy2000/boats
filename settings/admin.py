from django.contrib import admin
from .models import Settings , Images , NewsLitter
# Register your models here.
admin.site.register(Settings)
admin.site.register(NewsLitter)
admin.site.register(Images)