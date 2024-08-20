from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', include("signup.urls")),
    path('index/', admin.site.urls),
]
