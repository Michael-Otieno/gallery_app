from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.main, name='main'),
    url('^search/',views.search,name='search'),
    url('^location/(?P<location>\w+)/',views.location,name='location')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
