from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, Http404
from . models import Tag
from django.template import Context, loader


def homepage(request):
    return HttpResponse('Hello (again) World!')


def htmltag(request):
    tag_list = Tag.objects.all()
    output = "<html>\n"
    output += "<head>\n"
    output += "<title>\n"
    output += "Wrong Way</title>\n"
    output += "<body>\n"
    output += "<h1> Tag List </h1>\n"
    output += "<ul>\n"
    for tag in tag_list:
        output += "<li>\n"
        output += tag.name
        output += "</li>\n"
    output += "</ul>\n"
    output += "</body>\n"
    output += "</head>\n"
    output += "</html>\n"
    return HttpResponse(output)


@login_required()
def tag_list_page(request):
    tag_list = Tag.objects.all()

    class UserData:
        name = request.user
        is_logged_in = request.user.is_authenticated

    template = loader.get_template('organizer/tag_list.html')
    context = {'tag_list': tag_list,
               'user': UserData,
               }
    output = template.render(context)
    return HttpResponse(output)


def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    template = loader.get_template('organizer/tag_details.html')
    context = {'tag': tag}
    output = template.render(context)
    return HttpResponse(output)
