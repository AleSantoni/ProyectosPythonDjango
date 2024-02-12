
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import include
from pages.urls import pages_patterns
from Profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns



urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include(pages_patterns)),
    path('admin/', admin.site.urls),
    #Path de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    #path del profiles
    path('profiles/', include(profiles_patterns)),
    #path del messenger
    path('messenger/', include(messenger_patterns)),
    
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)