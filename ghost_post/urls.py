from django.contrib import admin
from django.urls import path
from ghost_post_app.views import index, post_form_view, boast, roast, up_vote, down_vote

urlpatterns = [
    path('', index, name="homepage"),
    path('boast/', boast),
    path('roast/', roast),
    path('upvote/<int:post_id>/', up_vote),
    path('downvote/<int:post_id>/', down_vote),
    path('postform/', post_form_view),
    path('admin/', admin.site.urls),
]

