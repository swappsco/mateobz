from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import api_views

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("home/", api_views.Home.as_view(), name="home"),
    path("questions/", api_views.QuestionList.as_view(), name="question-list"),
    path(
        "questions/<int:pk>/",
        api_views.QuestionDetail.as_view(),
        name="question-detail",
    ),
    path("choices/", api_views.ChoiceList.as_view(), name="choice-list"),
    path("choices/<int:pk>/", api_views.ChoiceDetail.as_view(), name="choice-detail"),
]
