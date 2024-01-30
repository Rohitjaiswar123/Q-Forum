from django.urls import path
from . import views
from .views import showinformation
from django.conf.urls import url
from .views import post_detail
urlpatterns =[
    path('' ,views.index, name ='index'),
    url(r'^AskaQuestion',views.showinformation, name= 'AskaQuestion'),
    url(r'^FAQ',views.openchatbot, name= 'FAQ'),
    url(r'^home',views.post_list,name ='home'),
    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.post_detail,name='post_detail'), 
    path('bot_search/' ,views.bot_search, name ='bot_search'),
    
    
]


