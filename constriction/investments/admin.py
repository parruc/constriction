from django.contrib import admin

from .models import Investment


class InvestmentAdmin(admin.ModelAdmin):
    class Meta:
        model = Investment


admin.site.register(Investment, InvestmentAdmin)
