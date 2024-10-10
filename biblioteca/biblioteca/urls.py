from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('/livros/')),  
    path('livros/', include('core.urls')),           
    path('admin/', admin.site.urls),
]