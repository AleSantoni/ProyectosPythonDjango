from core import views as core_views
from portfolio import views as portfolio_views
from django.contrib import admin
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('', core_views.home, name='home'),
    path('about-me/', core_views.about, name='about'),
    path('portfolio/', portfolio_views.portfolio, name='portfolio'),
    path('contact/', core_views.contact, name='contact'),

    path('admin/', admin.site.urls),
]

# esto es para servir los ficheros staticos asi pudo ver las imagenes cargadas de los proyectos
if settings.DEBUG:
    from django.conf.urls.static import static  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)