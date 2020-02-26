from django.contrib import admin
from churchacts.models import Person, PastoralCare, Ministry, Meeting, MeetingParticipant


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', '__unicode__')


class PastoralCareAdmin(admin.ModelAdmin):
    list_display = ('pastor', 'member')


class MinistryAdmin(admin.ModelAdmin):
    list_display = ('member', 'description', 'start_time')


class MeetingAdmin(admin.ModelAdmin):
    list_display = ('type', 'start_time')


class MeetingParticipantAdmin(admin.ModelAdmin):
    list_display = ('id', 'meeting')


admin.site.register(Person, PersonAdmin)
admin.site.register(PastoralCare, PastoralCareAdmin)
admin.site.register(Ministry, MinistryAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(MeetingParticipant, MeetingParticipantAdmin)
