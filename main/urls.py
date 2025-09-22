from django.urls import path
from . import views

urlpatterns = [
    path('review_create', views.ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_create'),
]