from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')),
    path('api/', include('reviews.urls')),  # API routes from your app
]
