from django.contrib import admin
from .models import Emp
admin.site.site_header = 'Mani Kumar'


class Empadmin(admin.ModelAdmin):
    list_display = ('eid','ename','esal','created','modified')
    list_filter = ('ename',)
    search_fields = ('ename',)

admin.site.register(Emp,Empadmin)