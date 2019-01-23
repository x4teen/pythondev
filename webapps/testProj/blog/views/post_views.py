from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from ..models import PostModel
from django.db.models import Q
from ..forms import PostModelForm
from django.urls import reverse
from django.contrib import messages


@login_required()
def list_posts(request):
    qs = PostModel.objects.all()
    query = request.GET.get("q", None)
    if query is not None:
        qs = qs.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(slug__icontains=query)
        )
    template = 'posts/list_posts.html'
    context = {'qs': qs}

    return render(request, template, context)


@login_required()
def show_post_detail(request, post_id):
    qs = get_object_or_404(PostModel, id=post_id)
    template = 'posts/show_post_detail.html'
    context = {'qs': qs}

    return render(request, template, context)


@login_required()
def add_post(request):
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        data = form.save(commit=False)
        data.save()
        messages.success(request, 'New Blog Post Created')
        return HttpResponseRedirect(reverse('show_post_detail', args=[str(data.id)]))

    template = 'posts/add_post.html'
    context = {'form': form}

    return render(request, template, context)


@login_required()
def edit_post(request, post_id):
    qs = get_object_or_404(PostModel, id=post_id)
    form = PostModelForm(request.POST or None, instance=qs)
    if form.is_valid():
        data = form.save(commit=False)
        data.save()
        messages.success(request, 'Updated Post')
        return HttpResponseRedirect(reverse('show_post_detail', args=[str(data.id)]))

    template = 'posts/edit_post.html'
    context = {'form': form,
               'post_id': post_id}
    return render(request, template, context)


@login_required()
def delete_post(request, post_id):
    qs = get_object_or_404(PostModel, id=post_id)
    if request.method == 'POST':
        message_delete_post = "Post '" + qs.title + "' was deleted."
        qs.delete()
        messages.success(request, message_delete_post)
        return HttpResponseRedirect(reverse('list_posts'))

    template = 'posts/delete_post.html'
    context = {'qs': qs,
               'post_id': post_id}

    return render(request, template, context)
