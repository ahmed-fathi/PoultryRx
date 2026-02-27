from django.urls import path

from apps.api.v1 import views


urlpatterns = [
    path("landing/featured", views.LandingFeaturedView.as_view(), name="landing-featured"),
    path("blog/", views.BlogListView.as_view(), name="blog-list"),
    path("articles/<slug:slug>/", views.ArticleDetailView.as_view(), name="article-detail"),
    path("profiles/<str:username>/public", views.ProfilePublicView.as_view(), name="profile-public"),
    path("library/", views.LibraryListView.as_view(), name="library-list"),
    path("faq/", views.FAQListView.as_view(), name="faq-list"),
    path("tools/", views.ToolsListView.as_view(), name="tools-list"),
]
