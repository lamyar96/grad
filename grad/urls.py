from django.conf.urls import url,include
from accounts.forms import SignupFormExtra
from django.contrib import admin
from app import urls as app_urls
from app import views
from django.conf import settings
from django.conf.urls.static import static
from userena import urls as userena_urls

urlpatterns = [
    url(r'^accounts/signup/$', 'userena.views.signup', {'signup_form': 'SignupFormExtra'}),
    url(r'^accounts/',include(userena_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^tw/',include(app_urls)),
    url(r'^$',views.Index),
]

if settings.DEBUG:
    urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"),
#    '/var/www/static/',
#]
