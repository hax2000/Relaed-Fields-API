from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('main/', include(('main.urls', 'main'), namespace='main')),
]
