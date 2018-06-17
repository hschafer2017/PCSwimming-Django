from django.conf.urls import url
from posts.views import get_posts

urlpatterns = [
    url(r'^posts/', get_posts, name='get_posts')
    ]
