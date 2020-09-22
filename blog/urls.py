from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from django.urls import path

urlpatterns = [
    path('',BlogListView.as_view(),name='blogs'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='blog_details'),
    path('post/new/', BlogCreateView.as_view(),name = 'create_blog'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='update_blog' ),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete_blog'),
    

]