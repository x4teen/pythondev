from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from ..models import PostModel
from ..forms import PostModeForm
from django.urls import reverse
from django.contrib import messages


@login_required()
def list_posts(request):
    qs = PostModel.objects.all()
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
    form = PostModeForm(request.POST or None)
    if form.is_valid():
        data = form.save(commit=False)
        data.save()
        messages.success(request, 'New Blog Post Created')
        return HttpResponseRedirect(reverse('show_post_detail', args=[str(data.id)]))

    template = 'posts/add_post.html'
    context = {'form': form}

    return render(request, template, context)
