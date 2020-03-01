from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from fitness_app.views import ProgramViewSet

router = routers.DefaultRouter()
router.register(r'programs', ProgramViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
