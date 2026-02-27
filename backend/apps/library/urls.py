from django.urls import path
from .views import LibraryListView, FAQListView

urlpatterns = [
    path('library/', LibraryListView.as_view(), name='library-list'),
    path('faq/', FAQListView.as_view(), name='faq-list'),
]
