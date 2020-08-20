from django.contrib import admin
from django.urls import path
from ghost_post_app.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
]
