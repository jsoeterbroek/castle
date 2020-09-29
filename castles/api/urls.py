from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import castle_list, castle_detail

urlpatterns = [
    path('castles', castle_list),
    path('castles/<int:pk>', castle_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)
