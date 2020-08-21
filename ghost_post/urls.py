from django.contrib import admin
from django.urls import path
from ghost_post_app.views import index, post_form_view, boast, roast

urlpatterns = [
    path('', index, name="homepage"),
    path('boast/', boast),
    path('roast/', roast),
    path('postform/', post_form_view),
    path('admin/', admin.site.urls),
]

