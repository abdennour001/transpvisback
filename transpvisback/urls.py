from django.contrib import admin
from django.urls import path, include


admin.site.site_header = 'Transpvis' + ' Creator v1'
admin.site.index_title = "Paramétrage"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("transparency.urls")),
]
