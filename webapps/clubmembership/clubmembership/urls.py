from django.contrib import admin
from django.urls import path, include
from .views import views, user_views, group_views, fee_views


user_patterns = [
    path('add/', user_views.add, name='add_user'),
    path('edit/<int:person_id>', user_views.edit, name='edit_user'),
    path('delete/<int:person_id>', user_views.delete, name='delete_user'),
    path('show/<int:person_id>', user_views.show, name='show_user'),
]

group_patterns = [
    path('add/', group_views.add, name='add_group'),
    path('edit/<int:group_id>', group_views.edit, name='edit_group'),
    path('delete/<int:group_id>', group_views.delete, name='delete_group'),
    path('show/<int:group_id>', group_views.show, name='show_group'),
]

fee_patterns = [
    path('add/', fee_views.add, name='add_fee'),
    path('edit/<int:fee_id>', fee_views.edit, name='edit_fee'),
    path('delete/<int:fee_id>', fee_views.delete, name='delete_fee'),
    path('show/<int:fee_id>', fee_views.show, name='show_fee'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),
    path('user/', include(user_patterns)),
    path('group/,', include(group_patterns)),
    path('fee/', include(fee_patterns)),
]
