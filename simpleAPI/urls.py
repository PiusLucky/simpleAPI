from django.contrib import admin
from django.urls import path
from .views import ListUUIDS

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/', ListUUIDS.as_view(), name="generate-uuids"),
]
