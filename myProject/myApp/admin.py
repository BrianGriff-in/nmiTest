from django.contrib import admin
from . models import Image, ImageQRCode, ImageIcons
# Register your models here.

admin.site.register(ImageQRCode)
admin.site.register(ImageIcons)