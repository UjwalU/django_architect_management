from django.contrib import admin
from .models import Architect, PortfolioItem, Project, Design, Payment
from django.utils.html import format_html


class MyModelAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title')

    def image_preview(self, obj):
        return format_html('<img src="{}" width="auto" height="150px" />', obj.image.url)
    image_preview.short_description = 'Image Preview'


admin.site.register(Architect)
admin.site.register(PortfolioItem,MyModelAdmin)
admin.site.register(Project)
admin.site.register(Design)
admin.site.register(Payment)

