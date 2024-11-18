from django.contrib import admin
from django.utils.html import format_html
from .models import Event, Participation

# Register the Event model in the admin panel
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'event_datetime', 'location', 'photo', 'view_participants')
    search_fields = ('title', 'location')
    list_filter = ('event_datetime', 'user')
    ordering = ('event_datetime',)

    def view_participants(self, obj):
        participants_count = obj.participation_set.count()
        return format_html(
            '<a href="{}">View Participants ({})</a>',
            f'/admin/events/participation/?event__id__exact={obj.id}',
            participants_count
        )

    view_participants.short_description = 'Participants'

# Register the Participation model in the admin panel
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'registered_at')
    search_fields = ('user__username', 'event__title')
    list_filter = ('event',)

admin.site.register(Event, EventAdmin)
admin.site.register(Participation, ParticipationAdmin)
