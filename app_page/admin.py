from django.contrib import admin
from app_page.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ['id','_domain','_title']
    save_on_top = True


admin.site.register(Page,PageAdmin)

