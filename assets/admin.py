from django.contrib import admin
from .models import RequestList, Equipment, Make, General, RequestDetails, Image
# Register your models here.

admin.site.register(RequestList)
admin.site.register(Equipment)
admin.site.register(Make)
admin.site.register(General)
admin.site.register(RequestDetails)
admin.site.register(Image)