"""phase6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from CoreBanking.views import LoginView, UserPanelView, CreateCenterView, CenterListView, CenterDeleteView, \
    CreateUserView, UserListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Login/$', LoginView.as_view(), name='login'),
    url(r'^UserPanel/$', UserPanelView.as_view(), name='user_panel'),
    url(r'^centercreate/$', CreateCenterView.as_view(), name='center_create'),
    url(r'^centerlist/$', CenterListView.as_view(), name='center_list'),
    url(r'^centerdelete/(?P<pk>\d+)/$', CenterDeleteView.as_view(), name='center_delete'),
    url(r'^createuser/$', CreateUserView.as_view(), name='create_user'),
    url(r'^userlist/$', UserListView.as_view(), name='user_list'),
]
