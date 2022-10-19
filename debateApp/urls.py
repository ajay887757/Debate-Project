
from django.urls import path , include
from .views import debateInfo
urlpatterns = [
    path('debateInfo/',debateInfo.as_view(),name="debateInfo"),
]
