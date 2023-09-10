from django.urls import path
from .views import videos_list, video_view

urlpatterns = [

    path('', videos_list, name='videos'),
    path('video/<str:video_hash>/', video_view, name='video'),

]
