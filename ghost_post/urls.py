from django.contrib import admin
from django.urls import path
from ghost_post_app.views import index, post_form_view

urlpatterns = [
    path('', index, name="homepage"),
    path('postform/', post_form_view),
    path('admin/', admin.site.urls),
]
