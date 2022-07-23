from ast import arg
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, View
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render


from .forms import PostForm
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "posts/home.html"


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post.html"
    success_url = reverse_lazy("home")


class ImageView(View):
    
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, "posts/image.html", {"post": post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if "run_script" in request.POST:

            # import function from the python file  
            # call function 
            post.ocr_text = "This will be the ocr text."
            post.save()
            # return HttpResponseRedirect(reverse("posts:image_extracted", args=(post.id, )))
            return HttpResponseRedirect(f"/posts/{post.id}/image_extracted/")
            


class ImageViewExtracted(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, "posts/image_extracted.html", {"post": post})
