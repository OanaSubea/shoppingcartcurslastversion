from django.conf.urls import url
from django.urls import path, re_path

from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^category/(?P<categoryid>\d+)/$', views.category_prodcut_list, name='product_list_by_category'),
    url(r'^product/(?P<productid>\d+)/$', views.product_detail, name='product_detail'), #aici se face maparea produsului
    re_path('^$', views.category_prodcut_list, name='product_list'),
    #url(r'^(?P<categoryid>\d+)/$', views.product_list, name='product_list_by_category'),
    #url(r'^(?P<productid>\d+)/$', views.product_detail, name='product_detail'),
]

#d+ = id numeric, il mapeaza la functia din views
#?P<nume_parametru> = asa stabilim parametrul functiei category_product_list
