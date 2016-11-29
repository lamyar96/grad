from django.conf.urls import url,include
from django.contrib import admin
from app import urls as app_urls
from app import views
from django.conf import settings
from django.conf.urls.static import static

url = [
    url(r'^admin/', admin.site.urls),
    url(r'^tw/',include(app_urls)),
    url(r'^$',views.Index),
]

if settings.DEBUG:
    url += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    url += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"),
#    '/var/www/static/',
#]
