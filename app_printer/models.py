from django.db import models
from django_markdown.models import MarkdownField


class Brand(models.Model):
    name = models.CharField(max_length=300)
    order_index = models.IntegerField(default=0)
    set_url = models.CharField(max_length=300)
    nation = models.CharField(max_length=300)
    logo_url = models.CharField(max_length=300)
    diver_url = models.CharField(max_length=300)
    description = MarkdownField()

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Brand Set'


class PrintType(models.Model):
    name = models.CharField(max_length=300)
    order_index = models.IntegerField(default=0)
    set_url= models.CharField(max_length=300)
    count_daily = models.CharField(max_length=300)
    description = MarkdownField()

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Type Set'


class Resolution(models.Model):
    resolution = models.CharField(max_length=300)

    def __str__(self):
        return self.resolution


    class Meta():
        verbose_name_plural = 'Resolution'


class MaxWidth(models.Model):
    max_width = models.CharField(max_length=300)

    def __str__(self):
        return self.max_width

    class Meta:
        verbose_name_plural = 'Max Width'


class RibbonSize(models.Model):
    ribbon_size = models.CharField(max_length=300)

    def __str__(self):
        return self.ribbon_size

    class Meta:
        verbose_name_plural = 'Ribbon Size'


class RibbonType(models.Model):
    ribbon_type = models.CharField(max_length=300)

    def __str__(self):
        return self.ribbon_type

    class Meta:
        verbose_name_plural = 'Ribbon Type'


class Article(models.Model):
    name = models.CharField(max_length=300)
    description = MarkdownField()
    set_url = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Article Related '

class Printer(models.Model):
    name = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    set_url = models.CharField(max_length=300)
    brand = models.ForeignKey(Brand)
    print_type = models.ForeignKey(PrintType)
    resolution = models.ForeignKey(Resolution)
    is_thermal_only = models.BooleanField(default=False)
    max_speed = models.CharField(max_length=300)
    max_width = models.ForeignKey(MaxWidth)
    memory_size = models.CharField(max_length=300)
    ribbon_size = models.ForeignKey(RibbonSize)
    ribbon_type = models.ForeignKey(RibbonType)
    weight = models.IntegerField(default=0)
    Printer_length= models.IntegerField(default=0)
    Printer_width= models.IntegerField(default=0)
    Printer_height= models.IntegerField(default=0)
    catalogue_url = models.CharField(max_length=300)
    diver_url = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    description = MarkdownField()
    img_url = models.CharField(max_length=300)
    img_banner = models.CharField(max_length=300)
    show_style = models.IntegerField(default=0)
    is_public = models.BooleanField(default=False)
    is_promotion = models.BooleanField(default=False)
    article = models.ForeignKey(Article)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Printers'
