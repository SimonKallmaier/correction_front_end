from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import OcrExtractedText


def index(request):
    return render(request, 'correction/index.html')

