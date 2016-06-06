from __future__ import unicode_literals

from django.conf import settings
from django.db import models

# Create your models here.

class User(models.Model):
	mob_user = models.OneToOneField(
		settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
	create_time = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.name

class Reseller(models.Model):
	mob_user = models.OneToOneField(
		settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
	tail = models.CharField(max_length=255, blank=True)
	create_time = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.name
	
class Dispatcher(models.Model):
	mob_user = models.OneToOneField(
		settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
	tail = models.CharField(max_length=255, blank=True)
	address = models.TextField()
	opening_time = models.IntegerField(max_length=11)
	closing_time = models.IntegerField(max_length=11)
	create_time = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.name

class Product(models.Model):
	title = models.CharField(max_length=200)
	desc = models.TextField()
	unit_price = models.IntegerField(max_length=11)
	market_price = models.IntegerField(max_length=11)
	spec = models.CharField(max_length=100)
	spec_desc = models.CharField(max_length=100)
	cover = models.ImageField(upload_to='images/product/%Y/%m/%d')
	is_snapshot = models.BooleanField(default=False)
	create_time = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		if self.is_snapshot:
			return '%s[SnapShot]' % self.title
		return self.title

class ProductDetails(models.Model):
	product = models.ForeignKey('Product')
	image = models.ImageField(upload_to='images/product_details/%Y/%m/%d')
	plain = models.TextField()
	seq = models.IntegerField(max_length=11)
	is_snapshot = models.BooleanField(default=False)
	create_time = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return '%s[%s]' % (self.product.title, self.seq)
	class Meta:
		verbose_name = 'Product details'
		verbose_name_plural = 'Product details'

class Bulk(models.Model):
	title = models.CharField(max_length=200)
	reseller = models.ForeignKey('Reseller')
	dispatchers = models.ManyToManyField('Dispatcher')
	products = models.ManyToManyField('Product')
	dead_time = models.DateTimeField()
	arrived_time = models.DateTimeField()
	status = models.IntegerField(max_length=11)
	card_title = models.CharField(max_length=100)
	card_desc = models.CharField(max_length=255)
	card_icon = models.ImageField(upload_to='images/card_icon/%Y/%m/%d', blank=True)
	create_time = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.title

class Order(models.Model):
	id = models.CharField(max_length=200, primary_key=True)
	user = models.ForeignKey('User')
	bulk = models.ForeignKey('Bulk')
	dispatcher = models.ForeignKey('Dispatcher')
	status = models.IntegerField(max_length=10)
	prepay_id = models.CharField(max_length=200)
	freight = models.IntegerField(max_length=11)
	total_fee = models.IntegerField(max_length=11)
	create_time = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return '%s(User: %s, Date: %s)' % (
			self.bulk.title, self.user.name, self.create_time)

class Goods(models.Model):
	user = models.ForeignKey('User') # TODO Remove it
	order = models.ForeignKey('Order')
	product = models.ForeignKey('Product')
	quantity = models.IntegerField(max_length=11)
	def __unicode__(self):
		return self.product.title
	class Meta:
		verbose_name = 'Goods'
		verbose_name_plural = 'Goods'

# Views

class PurchasedProductHistory(models.Model):
	order = models.ForeignKey('Order', primary_key=True)
	product = models.ForeignKey('Product')
	bulk = models.ForeignKey('Bulk')
	mob_user = models.ForeignKey(settings.AUTH_USER_MODEL)
	name = models.CharField(max_length=100, null=True, blank=True)
	quantity = models.IntegerField(max_length=11)
	spec = models.CharField(max_length=100)
	create_time = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'view_history_purchased_products'


