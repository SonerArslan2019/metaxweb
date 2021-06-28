from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Automatic_Doors)
admin.site.register(Hospital_Doors)
admin.site.register(Security_Doors)
admin.site.register(Request_Messages)
admin.site.register(Failure_Notification)
admin.site.site_title = "ARSLAN YAPI"
admin.site.site_header = "ARSLAN YAPI | METAXDOOR"
admin.site.index_title = "Admin Paneli"


