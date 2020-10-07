from django.conf.urls import url
from .import views
app_name='goto'
urlpatterns=[url(r'^$',views.index,name='index'),
             url(r'^entry/$',views.product_entry_page,name='product_entry_page'),
             url(r'^search/$',views.search,name='search'),
             url(r'^search/(?P<pk>[-\w]+)/del/$',views.del_object,name='del_object'),
             url(r'^search/(?P<pk>\d+)/edit/$',views.edit,name='edit'),
             url(r'^search/result/',views.result,name='result'),
             url(r'^setting/$',views.setting,name='setting')
             ]
