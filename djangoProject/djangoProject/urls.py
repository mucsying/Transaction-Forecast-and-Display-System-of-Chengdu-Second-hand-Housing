from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.home),
    url(r'^forecast$', views.forecast),
    url(r'^recommend$', views.recommend),
    url(r'^visualization$', views.visualization)
]

'''
py manage.py runserver 0.0.0.0:8000
'''