from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display =('name','email','message','created_at')
    search_fields =('name','email')
    list_filter =('created_at',)
admin.site.register(Contact, ContactAdmin)
