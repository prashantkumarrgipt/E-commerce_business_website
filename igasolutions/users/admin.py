from django.contrib import admin
from .models import *
# Register your models here.
class newsletterAdmin(admin.ModelAdmin):
    list_display=('id','name','email','number','service_options','specialNotes')
admin.site.register(newsletter,newsletterAdmin)


class contactusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','email','subject','message')
admin.site.register(contactus,contactusAdmin)


class productAdmin(admin.ModelAdmin):
    list_display=('id','title','image')
admin.site.register(product,productAdmin)