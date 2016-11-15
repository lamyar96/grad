from django.conf.urls import url,include
from django.contrib import admin
from app import urls as app_urls
from app import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tw/',include(app_urls)),
    url(r'^$',views.Index),
]
