
from django.contrib import admin
from django.urls import path, include
from blog.views import views
from blog.views import post_views


debugpatterns = [
    path('show/request', views.show_request, name='show_request'),
    path('show/response', views.show_response, name='show_response'),

]

postpatterns = [
    path('list', post_views.list_posts, name='list_posts'),
    path('detail/<int:post_id>', post_views.show_post_detail, name='show_post_detail'),
    path('add', post_views.add_post, name='add_post'),
    path('edit/<int:post_id>', post_views.edit_post, name='edit_post'),
    path('delete/<int:post_id>', post_views.delete_post, name='delete_post'),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home_page'),
    path('debug/', include(debugpatterns)),
    path('posts/', include(postpatterns)),
]
