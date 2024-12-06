from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<str:number>/', views.module, name='module'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)