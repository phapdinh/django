from django.conf.urls import include, url
from django.contrib import admin
from inventory import views

urlpatterns = [
    url(r'^$', views.index, name='list'),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]