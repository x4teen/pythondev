from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from . models import Post
from django.template import Context, loader
from .forms import PostForm
from django.contrib import messages


def homepage(request):
    return HttpResponse('Hello (again) World!')


@login_required()
def blog_list_page(request):
    blog_list = Post.objects.all()

    class UserData:
        name = request.user
        is_logged_in = request.user.is_authenticated

    template = 'blog/blog_list.html'
    context = {'blog_list': blog_list,
               'user': UserData,
               }
    return render(request, template, context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Post, id=blog_id)
    template = 'blog/blog_details.html'
    context = {'blog': blog}
    return render(request, template, context)


def blog_create(request):
    form = PostForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        messages.success(request, "Created a new blog post")
        # context = {"form": PostForm()}
        return HttpResponseRedirect("/blog/{num}".format(num=post.id))

    template = 'blog/blog_create.html'
    return render(request, template, context)


def blog_update(request, blog_id=None):
    blog = get_object_or_404(Post, id=blog_id)
    form = PostForm(request.POST or None, instance=blog)
    context = {
        'blog': blog,
        'form': form
    }

    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        messages.success(request, "Updated blog post")
        # context = {"form": PostForm()}
        return HttpResponseRedirect("/blog/{num}".format(num=post.id))

    template = 'blog/blog_update.html'
    return render(request, template, context)


def blog_delete(request, blog_id):
    blog = get_object_or_404(Post, id=blog_id)
    if request.method == "POST":
        blog.delete()
        messages.success(request, "Blog post was deleted")
        return HttpResponseRedirect("/blog")

    template = 'blog/blog_delete.html'
    context = {'blog': blog}
    return render(request, template, context)
