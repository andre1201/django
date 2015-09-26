from django.conf.urls import url
from publisher.views import PublisherList, PublisherDetail
from publisher.views import PublisherBookList

urlpatterns = [
    url(r'^$', PublisherList.as_view(),name='publisher'),
    url(r'^books/([\w-]+)/$', PublisherBookList.as_view()),
    url(r'^PublisherDetail/([\w-]+)/$', PublisherDetail.as_view()),
]