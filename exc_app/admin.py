from django.contrib import admin
from .models import User
from .forms import UserForm


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    fields = ("jméno", "email", "ičo")
    form = UserForm

    def has_add_permission(self, request):
        return False
