from django.conf.urls import url
from app import views
urlpatterns = [
    # /organization/id or /organization/
    url(r'^$',views.list_event,name='list_event'),#put the id here:   url(r'^(?P<post_id>\d+)/$',views
    url(r'^welcome$',views.home_page,name='home_page'),
    url(r'^(?P<organization_id>\d+)/$',views.show_organization,name='show_organization'),
     url(r'^following',views.list_followed_organizations,name='list_followed_organizations'),
]
