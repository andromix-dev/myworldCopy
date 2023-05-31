from django.urls import path
from . import views
from django.urls import path
from .views import upload_photo, photo_list

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.main, name='main'),
	path('members/', views.members, name='members'),
	path('members/details/<slug:slug>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('upload/', upload_photo, name='upload_photo'),
    path('photos/', photo_list, name='photo_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)