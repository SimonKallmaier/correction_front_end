import datetime

from django.db import models
from django.utils import timezone


class OcrExtractedText(models.Model):
    text = models.TextField()

    def __str__(self) -> str:
        return self.text
