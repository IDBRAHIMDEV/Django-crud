from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "username",
        "email",
        "state",
        "created",
    )
    list_filter = ("state",)
    search_fields = (
        "name",
        "username",
        "email",
    )


admin.site.register(Profile, ProfileAdmin)
