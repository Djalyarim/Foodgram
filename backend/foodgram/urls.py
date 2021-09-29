from django.contrib import admin
from django.urls import include, path

apipatterns = [
    path('', include('users.urls')),
    path('', include('recipes.urls')),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(apipatterns)),
]
