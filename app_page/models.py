from django.db import models
import uuid


class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    _domain = models.CharField(max_length=300,blank=True)
    _title = models.CharField(max_length=300,blank=True)
    _logo = models.CharField(max_length=300,blank=True)
    _visit_count = models.CharField(max_length=300,blank=True)

    def __str__(self):
        return self._domain
