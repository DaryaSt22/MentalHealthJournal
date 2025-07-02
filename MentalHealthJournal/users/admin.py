from django.contrib import admin
from .models import User, Profile, EmailVerification

admin.site.register(User)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'goals', 'stress_level', 'avatar')
    fields = ('user', 'gender', 'goals', 'stress_level', 'avatar')
    search_fields = ('user',)
    ordering = ('user',)


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration')
    fields = ('code', 'user', 'expiration', 'created')
    readonly_fields = ('created',)
