#!/usr/bin/python

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^([0-9]*)$', views.index, name='index'),
	url(r'^pay/cb/[0-9]*$', views.pay_callback, name='pay_callback'),
	url(r'^confirm$', views.confirm, name='confirm'),
	url(r'^confirm1$', views.confirm1, name='confirm1'),
]