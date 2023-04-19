from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    date = models.DateTimeField(auto_now_add = True)
    is_published = models.BooleanField(default=True)
