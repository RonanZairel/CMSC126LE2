from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from . import views
from django.contrib import admin

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('admin/', admin.site.urls),    
    path('', include(router.urls)),
]
