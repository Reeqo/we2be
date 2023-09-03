from django.urls import path
from feed.views import videos_list


urlpatterns = [

    path('', videos_list, name='videos')

]