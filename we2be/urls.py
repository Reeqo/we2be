from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [path('', include('feed.urls')),
               path('admin/', admin.site.urls),
               # path('register', include('register.urls')),
               # path('comment', include('comment.urls')),
               # path('upload', include('upload.urls')),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
