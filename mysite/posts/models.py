# posts/models.py
from django.db import models


class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    ocr_text = models.TextField(default="")

    def __str__(self):
        return self.title
