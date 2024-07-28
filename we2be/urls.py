from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import logout_then_login, LoginView, LogoutView
from django.urls import path, include

urlpatterns = [path('register/', include('register.urls')),
               path('admin/', admin.site.urls),
               path('', include('feed.urls')),
               path('login/', LoginView.as_view(), name='login'),
               path('logout/', LogoutView.as_view(), name='logout'),
               path('logout-then-login/', logout_then_login, name='logout_then_login'),
               # path('comment', include('comment.urls')),
               # path('upload', include('upload.urls')),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
