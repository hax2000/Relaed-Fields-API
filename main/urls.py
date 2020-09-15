from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as auth_views
from . import views

urlpatterns = [
    # props
    path('upload/', views.MainTableUploadView.as_view({'post': 'upload_records'}), name='upload_records'),

    # auth
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', auth_views.obtain_auth_token, name='api_token_auth'),

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
