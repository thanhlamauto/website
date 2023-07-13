from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Book
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
import markdown2
import random
from datetime import datetime
import pytz
from django.core.paginator import Paginator


def index(request):
    return render(request, 'website/index.html')

def resources(request):
    if request.method == "GET":
        books = Book.objects.all()
        return render(request, 'website/resources.html', {
            "books": books,
        })

def displayCategory(request):
    if request.method == "POST":
        tag = request.POST['category']
        Allposts = Post.objects.all()
        if tag == "All":
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(tag=tag)
        #Pagination
        paginator = Paginator(posts, 9)
        page_number = request.GET.get('page')
        posts_of_the_page = paginator.get_page(page_number)
        # Randomly select 5 posts from the filtered posts
        suggested_posts = random.sample(list(Allposts), 5)
        return render(request, 'website/blog.html', {
            "posts": posts,
            "posts_of_the_page": posts_of_the_page,
            "suggested_posts": suggested_posts
        })
    

def blog(request):
    if request.method == "GET":
        posts = Post.objects.all()
        #Pagination
        paginator = Paginator(posts, 9)
        page_number = request.GET.get('page')
        posts_of_the_page = paginator.get_page(page_number)
        # Randomly select 5 posts from the filtered posts
        suggested_posts = random.sample(list(posts), 5)
        return render(request, 'website/blog.html', {
            "posts": posts,
            "posts_of_the_page": posts_of_the_page,
            "suggested_posts": suggested_posts
        })

def post_detail(request, post_id):
    article = Post.objects.get(pk=post_id)
    markdown_content = article.content
    html_content = markdown2.markdown(markdown_content)
    return render(request, 'website/blog_detail.html', {'article': article, 'html_content': html_content})
        
def create_post(request):
    if request.method == "GET":
        return render(request, 'website/create_post.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        tag = request.POST.get('tag')
        photo = request.FILES.get('image')  # Get the uploaded image

        # Create a new Post instance
        post = Post(title=title, content=content, photo=photo, tag=tag)

        # Save the post to the database
        post.save()

        return redirect("blog")  # Redirect to the home page or a success page
        
    

    
    



