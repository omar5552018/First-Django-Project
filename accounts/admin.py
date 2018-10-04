from django.contrib import admin
from accounts.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'Jobs', 'city', 'phone', 'website')

    def Jobs(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-city', 'description')
        return queryset


admin.site.register(UserProfile, UserProfileAdmin)
