from django.contrib import admin
from django.urls import path, include
from notes.views import home_redirect  # import your redirect view

urlpatterns = [
    path('', home_redirect, name='home'),  # root URL → login
    path('notes/', include('notes.urls')),  # your app URLs
    path('admin/', admin.site.urls),
]



