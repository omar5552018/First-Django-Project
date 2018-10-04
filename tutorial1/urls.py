from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url('admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^home/', include('home.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

