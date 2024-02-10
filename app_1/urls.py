from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name = 'about'),
    path('heads/', views.heads_or_tails,name='heads_or_tails'),
    path('dice/', views.dice, name='dice'),
    path('digit/', views.digit, name='digit'),
    path('authors/', views.authors_view, name='authors'),
    path('posts/', views.posts_view, name='posts'),
    path('heads3/<int:count>', views.heads_or_tails3,name='heads_or_tails3'),
    path('dice3/<int:count>', views.dice3, name='dice3'),
    path('digit3/<int:count>', views.digit3, name='digit3'),
    path('author_post/<int:author_id>',views.author_post, name='author_post'),
    path('post/<int:post_id>',views.post_view,name='post_view'),
    path('game/',views.choose_game,name='game'),
    path('author/',views.author_add,name='author'),
    path('post/',views.post_add,name='post'),
]