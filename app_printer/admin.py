from django.contrib import admin
from app_printer.models import Brand, PrinterType, Article, Printer


class PrinterAdmin(admin.ModelAdmin):
    list_display = ['id','name','brand','printer_type','resolution']
    save_on_top = True


admin.site.register(Brand)
admin.site.register(PrinterType)
admin.site.register(Article)
admin.site.register(Printer,PrinterAdmin)
