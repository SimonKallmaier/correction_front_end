from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import OcrExtractedText


class IndexView(generic.DetailView):
    template_name = "correction/index.html"
    model = OcrExtractedText


class TextView(generic.ListView):
    template_name = "correction/show_text.html"
    context_object_name = "ocr_text"
    
    def get_queryset(self):
        return OcrExtractedText.objects.order_by('-pub_date')[-1]
