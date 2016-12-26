from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^add_item$', views.add_item, name="add_item"),
    url(r'^for_sale$', views.all_items, name="all_items"),
    url(r'^item/([0-9]+)', views.item_detail, name="item"),
    url(r'^update_profile$', views.update_profile, name="update_profile"),
]
