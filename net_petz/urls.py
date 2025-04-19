from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pets'

urlpatterns = [
    path('', views.net_petz_list, name="list"),
    path('<slug:slug>/feed/', views.feed_pet, name="feed"),
    path('<slug:slug>', views.net_petz_page, name="page"),
    path('<slug:slug>/upload/', views.upload_pet_image, name='upload'),
    path('<slug:slug>/rename/', views.update_pet_name, name='rename'),
    path('create/', views.create_pet, name='create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)