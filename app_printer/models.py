from django.db import models
from django_markdown.models import MarkdownField


class CBase(models.Model):
    name = models.CharField(max_length=300)
    order_index = models.IntegerField(default=0)
    title = models.CharField(max_length=300,blank=True)
    meta_description = models.TextField(blank=True)
    page_url = models.CharField(max_length=300,blank=True)
    img_url = models.CharField(max_length=300,blank=True)
    description = MarkdownField(blank=True)

    def __str__(self):
        return self.name

class Brand(CBase):
    nation = models.CharField(max_length=300)
    diver_url = models.CharField(max_length=300)

    class Meta():
        verbose_name_plural = 'Brand Set'


class PrinterType(CBase):
    count_daily = models.CharField(max_length=300,default='4000')


    class Meta():
        verbose_name_plural = 'Type Set'

class Article(CBase):
    class Meta:
        verbose_name_plural = 'Article Related '

class Printer(CBase):
    RESOLUTION_CHOICE = (('200','200 dpi'),('300','300 dpi'),('400','400 dpi'),('600','600 dpi'))
    RIBBON_TYPE_CHOICE = (('0','外碳'),('1','内碳'),('2','外碳和内碳'),('3','无'))
    RIBBON_SIZE_CHOICE = (('0','大卷芯 (25.4 mm)'),('1','小卷芯 (12.7 mm)'),('3','其他'))
    MAXWIDTH_CHOICE = (('0','4 英寸'),('1','6 英寸'),('2','2 英寸'),('3','其他'))

    brand = models.ForeignKey(Brand)
    printer_type = models.ForeignKey(PrinterType)
    resolution = models.CharField(max_length=3,choices=RESOLUTION_CHOICE,default='200')
    is_thermal_only = models.BooleanField(default=False)
    max_speed = models.CharField(max_length=300,blank=True)
    max_width = models.CharField(max_length=3,choices=MAXWIDTH_CHOICE,default='0')
    memory_size = models.CharField(max_length=300,blank=True)
    ribbon_size = models.CharField(max_length=3,choices=RIBBON_SIZE_CHOICE,default='0')
    ribbon_type = models.CharField(max_length=3,choices=RIBBON_TYPE_CHOICE,default='0')
    weight = models.IntegerField(default=0)
    Printer_length= models.IntegerField(default=0,blank=True)
    Printer_width= models.IntegerField(default=0,blank=True)
    Printer_height= models.IntegerField(default=0,blank=True)
    catalogue_url = models.CharField(max_length=300,blank=True)
    diver_url = models.CharField(max_length=300,blank=True)
    price = models.IntegerField(default=0)
    img_banner = models.CharField(max_length=300,blank=True)
    show_style = models.IntegerField(default=0)
    is_public = models.BooleanField(default=False)
    is_promotion = models.BooleanField(default=False)
    article = models.ManyToManyField(Article,blank=True)


    class Meta:
        verbose_name_plural = 'Printers'
