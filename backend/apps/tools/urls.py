from django.urls import path
from .views import ToolListView

urlpatterns = [
    path('tools/', ToolListView.as_view(), name='tool-list'),
]
