from django.urls import include, path
from rest_framework.routers import DefaultRouter

from main.views import ReadCardViewset, UploadedFileViewSet

router = DefaultRouter()
router.register('cards', ReadCardViewset)
router.register('files', UploadedFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
