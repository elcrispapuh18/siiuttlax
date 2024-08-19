
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.home.urls')),
    path('academy/', include('apps.academy.urls')),
    path('admin/', admin.site.urls),
    path('periods/', include('apps.period.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
