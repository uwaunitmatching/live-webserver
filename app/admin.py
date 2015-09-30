from django.contrib import admin
from app.models import Units, University, Keywords

class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit_code', 'unit_name', 'show_unit_link')
    search_fields = ('unit_code', 'unit_name')
    def show_unit_link(self, obj):
        return '<a href="%s">%s</a>' % (obj.unit_link, obj.unit_link) 
    show_unit_link.allow_tags = True

class UniAdmin(admin.ModelAdmin):
    list_display = ('uni_name', 'country', 'times_ranking', 'show_uni_link')
    search_fields = ('unit_code', 'unit_name')
    def show_uni_link(self, obj):
        return '<a href="%s">%s</a>' % (obj.uni_link, obj.uni_link) 
    show_uni_link.allow_tags = True

admin.site.register(Units, UnitAdmin)
admin.site.register(University, UniAdmin)
admin.site.register(Keywords)