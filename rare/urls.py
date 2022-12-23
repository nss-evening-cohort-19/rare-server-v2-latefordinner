from django.contrib import admin
from django.urls import path
from rareapi.views import register_user, check_user
from django.conf.urls import include
from rest_framework import routers
from rareapi.views import PostView, CategoryView, TagView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'posts', PostView, 'posts')
router.register(r'tags', TagView, 'tag')
router.register(r'categories', CategoryView, 'category')

urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
