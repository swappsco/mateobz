from django.urls import path
from .api_views import PollListView, PollDetailView

urlpatterns = [
    path("polls/", PollListView.as_view(), name="poll-list"),
    path("polls/<int:pk>/", PollDetailView.as_view(), name="poll-detail"),
]
