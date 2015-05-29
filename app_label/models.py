from django.db import models
from django_markdown.models import MarkdownField

class Material(models.Model):
    name = models.CharField(max_length=100)
    imgUrl = models.CharField(max_length=100)
    setUrl = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

class Width(models.Model):
    width = models.CharField(max_length=100)

    def __str__(self):
        return self.width

class Height(models.Model):
    height = models.CharField(max_length=100)

    def __str__(self):
        return self.height

class Label(models.Model):
    setUrl = models.CharField(max_length=100, db_index=True)
    material = models.ForeignKey(Material)
    width = models.ForeignKey(Width)
    height = models.ForeignKey(Height)
    count = models.IntegerField(default=2000)
    is_show = models.BooleanField(default=False)
    is_stock = models.BooleanField(default=False)
    description = MarkdownField()

    def __str__(self):
        return '{0} ({1}mm * {2}mm)'.format(str(self.material), str(self.width), str(self.height))


    class Meta:
        verbose_name = 'Label'
        unique_together = ('material', 'width', 'height', 'id')

