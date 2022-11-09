
from django.urls import path , include
from .views import debateInfo,readDebateList,PostNewDebate
urlpatterns = [
    path('debateInfo/',debateInfo.as_view(),name="debateInfo"),
    path('readDebateList/',readDebateList.as_view(),name="readDebateList"),
    path('PostNewDebate/',PostNewDebate.as_view(),name="PostNewDebate"),
]
