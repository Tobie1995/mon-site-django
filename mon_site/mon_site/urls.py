
from django.contrib import admin
from django.urls import path
from hello import views as hello_views
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_views.bonjour, name='bonjour'),
]
