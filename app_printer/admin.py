from django.contrib import admin
from app_printer.models import Brand, PrintType, Resolution, MaxWidth, RibbonSize, RibbonType, Article, Printer


admin.site.register(Brand)
admin.site.register(PrintType)
admin.site.register(Resolution)
admin.site.register(MaxWidth)
admin.site.register(RibbonSize)
admin.site.register(RibbonType)
admin.site.register(Article)
admin.site.register(Printer)
