from django.conf.urls import url,includ
from app import views
urlpatterns = [
    # /organization/id or /organization/
    url(r'^$',views.list_organization,name='list_organization'),#put the id here:   url(r'^(?P<post_id>\d+)/$',views
]
