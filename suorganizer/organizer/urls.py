from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage),
    path('tag', views.tag_list_page),
    path('tag/<int:tag_id>', views.tag_detail, name='detail'),


]
