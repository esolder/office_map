from django.contrib import admin

from .models import Plan, Workplace


class WorkplaceInline(admin.TabularInline):
    model = Workplace


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    inlines = [WorkplaceInline]
    fields = ['name', 'img']
