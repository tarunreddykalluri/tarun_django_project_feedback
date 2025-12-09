from django.contrib import admin
from django.urls import path
from myapp.views import feedbackview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feed/', feedbackview),
]
