from django.contrib import admin
from django.urls import path
from .views import ListUUIDS

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'/', ListUUIDS.as_view(), name="generate-uuids"),
]
