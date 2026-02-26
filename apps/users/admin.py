from django.contrib import admin
from apps.users.models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'unique_id', 'age', 'gender']
    # Rather than Showing UserProfile Object 1, data in admin panel is shown in tabular format with above Cols.
    