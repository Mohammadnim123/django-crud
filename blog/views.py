from django.shortcuts import render
from django.urls import reverse_lazy , reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.

class BlogListView(ListView):
    template_name = 'blogs.html'
    model = Post

class BlogDetailView(DetailView):
    template_name = 'blog_details.html'
    model = Post

class BlogCreateView(CreateView):
    template_name = 'create_blog.html'
    model = Post
    fields = ['title','author','body']
    
class BlogUpdateView(UpdateView):
    template_name = 'update_blog.html'
    model = Post
    fields = ['title','author','body']

class BlogDeleteView(DeleteView):
    template_name = 'delete_blog.html'
    model = Post
    success_url = reverse_lazy('blogs')