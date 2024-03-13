from . import views
from django.urls import path
from blog.views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    # path("", views.index, name="index"),
    path('', PostListView.as_view(), name='index'),
    path('new/', PostCreateView.as_view(), name='create'),
    # path("<int:post_id>/", views.detail, name="detail"),
    path('<int:post_id>/', PostDetailView.as_view(), name='detail'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
]