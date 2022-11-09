
from django.urls import path , include
from .views import debateInfo,readDebateList,PostNewDebate,customLogin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [
    path('debateInfo/',debateInfo.as_view(),name="debateInfo"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("Custom/login/", customLogin.as_view(), name="login"),

    path('readDebateList/',readDebateList.as_view(),name="readDebateList"),
    path('PostNewDebate/',PostNewDebate.as_view(),name="PostNewDebate"),
]
