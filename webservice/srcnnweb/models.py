from django.db import models

class ImageControl(models.Model):
    image_name = models.CharField(max_length=200)
    status = models.IntegerField(default=0)
    def __str__(self):
      return self.image_name
    def get_status(self):
      return self.status
