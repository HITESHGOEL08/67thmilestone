from django.contrib import admin

# Register your models here.
from website.models import Campus_Ambassdors, Sponsors, Team, Events, UserProfile, single_event

class CampusAmbassdorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('email',)}

class SponsorsAdmin(admin.ModelAdmin):
    pass

class TeamAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class UserAdmin(admin.ModelAdmin):
    pass

class SingleEventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Campus_Ambassdors, CampusAmbassdorAdmin)
admin.site.register(Sponsors, SponsorsAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Events, EventAdmin)
admin.site.register(UserProfile, UserAdmin)
admin.site.register(single_event, SingleEventAdmin)