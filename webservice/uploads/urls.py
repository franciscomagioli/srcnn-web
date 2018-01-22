from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from uploads.core import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
	url(r'^admin/', admin.site.urls),
	url(r'^detail/(?P<document_id>[0-9]+)/$', views.detail, name ='detail'),
		]