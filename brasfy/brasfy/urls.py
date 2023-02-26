
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('myapp.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)







