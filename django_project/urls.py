from django.contrib import admin
from django.urls import path, include  # new

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),
    # User management
    # Local app
    path("", include("pages.urls")),
]
