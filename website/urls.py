from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'website'

urlpatterns = [
    path("", views.index, name="index"),
    path("blog", views.blog, name="blog"),
    path('detail-page/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create-post', views.create_post, name='create_post'),
    path('displayCategory', views.displayCategory, name="displayCategory"),
    path('resources', views.resources, name="resources")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)