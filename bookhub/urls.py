from django.contrib import admin
from django.urls import path, include
#from django.http import HttpResponse

urlpatterns = [
    #path('', lambda request: HttpResponse("Welcome to BookHub API")),  # Root path
    path('admin/', admin.site.urls),
    path('api/', include('reviews.urls')),  # API routes from your app
]
