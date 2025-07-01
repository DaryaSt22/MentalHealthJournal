from django.contrib import admin
from .models import JournalEntry

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'mood', 'date')
    list_filter = ('mood', 'date', 'user')
    search_fields = ('user',)