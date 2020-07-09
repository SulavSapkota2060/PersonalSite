from django.shortcuts import render
from .models import *
from .forms import *
from .filters import SearchForm

def index(request):
    template = 'blogSite/index.html'
    posts = BlogPost.objects.all().order_by('-date_created')[:4]
    active_project = Projects.objects.filter(status='Active')
    context = {
        'posts': posts,
        'active':active_project
    }

    return render(request, template, context)


def content(request, pk):
    template = 'blogSite/content.html'
    post = BlogPost.objects.get(id=pk)
    commentForm = CommentForm()
    allComments = Comment.objects.filter(post_id=post)
    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid:
            y = commentForm.save()
            y.post_id = post
            y.save()
    context = {
        'post': post,
        'commentForm': commentForm,
        'allComments': allComments
    }
    return render(request, template, context)


def projects(request):
    template = 'blogSite/projects.html'
    active_project = Projects.objects.filter(status='Active')
    finished_project = Projects.objects.filter(status='Accomplished')
    context = {
        'acp':active_project,
        'accp':finished_project,
    }
    return render(request,template,context)


def teams(request):
    template = 'blogSite/team.html'
    context = {

    }
    return render(request,template,context)


def AllPost(request):
    posts = BlogPost.objects.all().order_by('-date_created')
    template = 'blogSite/blog.html'
    search = SearchForm(request.GET, queryset=posts)
    posts = search.qs
    context = {
        'posts':posts,
        'sform':search,
    }
    return render(request,template,context)


def contact(request):
    template = 'blogSite/contact.html'
    context = {

    }
    return render(request,template,context)

