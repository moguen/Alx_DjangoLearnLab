from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name="register"),
    path('profile/', views.profile_view, name = 'profile'),
     path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/edit/', views.edit_profile_view, name = 'profile_edit'),
    path('post_list/', views.PostListView.as_view(), name='post_list'),
    path('post_detail/<pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comments/new/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comment/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('search/', views.PostSearchView.as_view(), name='post_search'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='tag_posts'),
]