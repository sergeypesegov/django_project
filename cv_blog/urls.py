from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='cv_blog_home'),
]