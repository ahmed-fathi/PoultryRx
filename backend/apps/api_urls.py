from django.urls import path
from apps.blog.views import featured_articles, blog_list, article_detail
from apps.profiles.views import public_profile
from apps.tools.views import tools_list
from apps.library.views import library_list
from apps.faq.views import faq_list

urlpatterns = [
    path('landing/featured', featured_articles, name='landing-featured'),
    path('blog/', blog_list, name='blog-list'),
    path('articles/<slug:slug>/', article_detail, name='article-detail'),
    path('profiles/<str:username>/public', public_profile, name='profile-public'),
    path('tools/', tools_list, name='tools-list'),
    path('library/', library_list, name='library-list'),
    path('faq/', faq_list, name='faq-list'),
]
