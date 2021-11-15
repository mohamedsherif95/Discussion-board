from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('boards/<int:pk>/', views.board_topics, name='board_topics'),
    path('boards/<int:pk>/new/', views.new_topic, name='new_topic'),
    path('boards/<int:board_pk>/topics/<int:topic_pk>', views.topic_posts, name='topic_posts'),
    path('boards/<int:board_pk>/topics/<int:topic_pk>/new', views.new_post, name='new_post'),
]
