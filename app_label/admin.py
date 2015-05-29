from django.contrib import admin
from app_label.models import Material, Width, Height, Label
from django_markdown.admin import MarkdownModelAdmin

admin.site.register(Material)
admin.site.register(Width)
admin.site.register(Height)
admin.site.register(Label, MarkdownModelAdmin)
