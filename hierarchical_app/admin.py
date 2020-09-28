from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from hierarchical_app.models import Folder
# from hierarchical_app.models import MyUser

# Register your models here.
admin.site.register(Folder, DraggableMPTTAdmin)
# admin.site.register(MyUser)