from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from servidor import views


urlpatterns=[
    path('api/',views.FloreViewSet.as_view()),
]
urlpatterns=format_suffix_patterns(urlpatterns)