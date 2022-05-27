from django.contrib import admin
from .models import Profile, Relationship

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['user', 'date_of_birth', 'photo']
admin.site.register(Profile)
admin.site.register(Relationship)