from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage),
    path('tag', views.tagpage),
    path('tag/<int:tag_id>', views.detail, name='detail'),


]
