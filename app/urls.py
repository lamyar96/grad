from django.conf.urls import url
from app import views
urlpatterns = [
    # /organization/id or /organization/
    url(r'^$',views.list_followed_organizations,name='list_followed_organizations'),#put the id here:   url(r'^(?P<post_id>\d+)/$',views
    url(r'^welcome$',views.home_page,name='home_page'),
]
