from django.urls import path
from cards import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('cards/', views.CardList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)