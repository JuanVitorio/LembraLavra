from django.urls import path, include
from . import views

app_name = 'words'

urlpatterns = [
    path('', views.home, name='home'),

    path('new/', views.word_create, name='create'),

    path('word/<int:pk>/',
         views.word_detail,
         name='detail'),

    path('word/<int:pk>/edit/',
         views.word_update,
         name='update'),

    path('word/<int:pk>/delete/',
         views.word_delete,
         name='delete'),

        # Categorias

path(
    'categories/',
    views.category_list,
    name='categories'
),

path(
    'categories/new/',
    views.category_create,
    name='category_create'
),

path(
    'categories/<int:pk>/delete/',
    views.category_delete,
    name='category_delete'
),

# Línguas

path(
    'languages/',
    views.language_list,
    name='languages'
),

path(
    'languages/new/',
    views.language_create,
    name='language_create'
),

path(
    'languages/<int:pk>/delete/',
    views.language_delete,
    name='language_delete'
),
]

