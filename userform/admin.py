from django.contrib import admin
from userform.models import Register

class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id','eno','ename','esal','eaddr']
admin.site.register(Register,RegisterAdmin)
