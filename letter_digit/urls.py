from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from letters.views import string_variations_list

urlpatterns = [
    path("wordvariations/", string_variations_list, name="wordvariations"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
