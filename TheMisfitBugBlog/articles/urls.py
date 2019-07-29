from django.urls import path, include
from . import views
from rest_framework import routers

# API Routers
router = routers.DefaultRouter()
router.register('comment', views.CommentView)

urlpatterns = [
    path('articles/create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('', views.FeaturedArticleListView.as_view(), name='featured_articles'),
    path('about/', views.about, name='about'),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('articles/edit/', views.ArticleEditListView.as_view(), name='article_edit_list'),
    path('articles/edit/update/<int:pk>/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('articles/edit/delete/<int:pk>/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('articles/<int:pk>/comments/', include(router.urls), name='comment_api'),
]