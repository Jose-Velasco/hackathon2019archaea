from django.urls import path
from .views import Index, UploadFiles

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("uploadfiles", UploadFiles.as_view(), name="uploadfiles")
]