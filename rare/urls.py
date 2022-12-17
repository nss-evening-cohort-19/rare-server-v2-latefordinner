from django.contrib import admin
from django.urls import path
from rareapi.views import register_user, check_user
from django.conf.urls import include
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
