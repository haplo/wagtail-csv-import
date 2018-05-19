from django.conf.urls import url

from wagtailcsvimport import views


app_name = 'wagtailcsvimport_admin'
urlpatterns = [
    url(r'^import_from_file/$', views.import_from_file, name='import_from_file'),
    url(r'^export_to_file/$', views.export_to_file, name='export_to_file'),
    url(r'^$', views.index, name='index'),
]
