from django.contrib import admin
from .models import Event, Ticket

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'venue', 'capacity', 'price', 'created_by')
    list_filter = ('date', 'venue')
    search_fields = ('title', 'description')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'event', 'user', 'purchase_date', 'is_cancelled')
    list_filter = ('is_cancelled', 'purchase_date')
    search_fields = ('ticket_number', 'user__username', 'event__title')