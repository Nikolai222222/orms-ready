
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include("clientes.urls")),
    path('autos/', include("autos.urls")),
    path('carro/', include('carro.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registro/login.html'), name='login'), 
    path('accounts/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)