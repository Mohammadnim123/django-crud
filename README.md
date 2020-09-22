# Blog_Project

[Repo](https://github.com/Mohammadnim123/django-crud)

[PR1](https://github.com/Mohammadnim123/django-crud/pull/1)

**Overview**

Add full CRUD functionality to your bag of tricks by building a Django project that allows Creating, Reading, Updating and Deleting.

**Feature Tasks and Requirements**

NOTE: replace blog and Post with your own names.

Create blog_project Django project

Create blog app

Create Post model

title field

author field

body field

Register model with admin

Create BlogListView that extends appropriate generic view
associated url path is an empty string

Create BlogDetailView that extends appropriate generic view
associated url path is `post/<int:pk>/`

Create BlogCreateView that extends appropriate generic view
associated url path is post/new/

Create BlogUpdateView that extends appropriate generic view
associated url path is `post/<int:pk>/edit/`

Create BlogDeleteView that extends appropriate generic view
associated url path is `post/<int:pk>/delete/`

Add urls to support all views, with appropriate names

Add templates to support all views

Add navigation links in appropriate locations to access all pages

Make all necessary changes to project level files for project to run

In other words, make it work.

