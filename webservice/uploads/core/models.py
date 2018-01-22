from __future__ import unicode_literals

from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)

class SrcnnImage(models.Model):
	document = models.FileField(upload_to='srcnn/')
	original = models.ForeignKey(Document, on_delete = models.CASCADE)

class BicubicImage(models.Model):
	document = models.FileField(upload_to='bicubic/')
	original = models.ForeignKey(Document, on_delete = models.CASCADE)