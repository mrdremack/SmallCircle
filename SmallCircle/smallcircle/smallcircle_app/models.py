from __future__ import unicode_literals
from django.contrib.auth.models import UserProfile, BaseUserManager, AbstractBaseUser
from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class MainPage(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title


class AccountManager(BaseUserManager):

	def create_user(self, email, password=None, **kwargs):
		if not email:
			raise ValueError('User must have a valid address.')
		if not kwargs.get('username'):
			raise ValueError('Users must have a valid username.')

		account = self.model( email=self.normalize_email(email), 
			username=kwargs.get('username')
			)

		account.set_password(password)

		account.save()

		return account 

	def create_superuser(self, email, password, **kwargs):
		account = self.create_user(email, password, **kwargs)

		account.is_admin = True

		account.save()

		return account


class Account(AbstractBaseUser):
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=40, unique=True)
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	tagline = models.CharField(max_length=40,blank=True)
	is_admin = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = AccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __unicode__(self):
		return self.email

	def get_full_name(self):
		return ' '.join(self.first_name, self.last_name)

	def get_short_name(self):
		return self.first_name


#class Category(models.Model):
#	user = models.ForeignKey(User)
#	name = models.CharField(max_length=128, unique=True)
#	likes = models.IntegerField(default=0)
#	slug = models.SlugField()


#	def save(self, *args, **kwargs):
#			self.slug = slugify(self.name)
#
#			if self.likes < 0:
#				self.likes = 0

#			super(Category, self).save(*args, **kwargs)
		
#	def __unicode__(self):
#		return self.name
		



class UserProfile(models.Model):
	#This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	#The additional attributes we wish to include.
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	bio = models.TextField(blank=True)

	#Override the __unicode__()method to return out something meaningful:
	def __unicode__(self):
		return self.user.username





class Audio(models.Model)
	user = models.ForeignKey(User)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

class Photos(models.Model)
	user = models.ForeignKey(User)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)



class Quotes(models.Model)
	user = models.ForeignKey(User)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)



class Videos(models.Model)
	user = models.ForeignKey(User)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)



class Miscellaneous(models.Model)
	user = models.ForeignKey(User)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

class View_all(models.Model)
	

