from django.urls import path
from .views import Index, UploadFiles, Debug

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("uploadfiles", UploadFiles.as_view(), name="uploadfiles"),
    path("debug", Debug.as_view(), name="debug")
]