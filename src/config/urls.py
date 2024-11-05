from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "TODO Admin"
admin.site.site_title = "TODO"
admin.site.index_title = "Welcome to TODO"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todo.urls")),
    path("api/", include("api.urls")),
]
