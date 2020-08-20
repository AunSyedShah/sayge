from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from emails.api import send_email as send_email_api
from rest_framework import routers
from stores.api import company_snapshot


router = routers.DefaultRouter()

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('api/emails', send_email_api, name='api-send-emails'),
    path('api/stores/company-snapshot', company_snapshot, name='api-stores-company-snapshot'),
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
]
