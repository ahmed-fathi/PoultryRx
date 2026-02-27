from django.urls import path
from .views import FeaturedArticlesView, BlogListView, ArticleDetailView, PublicProfileView

urlpatterns = [
    path('landing/featured', FeaturedArticlesView.as_view(), name='landing-featured'),
    path('blog/', BlogListView.as_view(), name='blog-list'),
    path('articles/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('profiles/<str:username>/public', PublicProfileView.as_view(), name='profile-public'),
]
