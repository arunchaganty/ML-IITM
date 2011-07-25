from django.conf.urls.defaults import *
from home.models import NewsItem
from endless_pagination.views import AjaxListView

urlpatterns = patterns('mliitm.home.views',
    (r'^news/(?P<news_id>[0-9]+)/$', 'news'),
    (r'^news/', 'news'),
    (r'', 'home'),
)
