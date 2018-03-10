from django.contrib import admin

# Register your models here.
from website.models import Campus_Ambassdors,Sponsors,Team


class CampusAmbassdorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('email',)}

class SponsorsAdmin(admin.ModelAdmin):
    pass

class TeamAdmin(admin.ModelAdmin):
    pass

admin.site.register(Campus_Ambassdors, CampusAmbassdorAdmin)
admin.site.register(Sponsors,SponsorsAdmin)
admin.site.register(Team,TeamAdmin)