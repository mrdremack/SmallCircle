from __future__ import unicode_literals
from django.contrib.auth.models import User 
from django.db import models
from embed_video.fields import EmbedVideoField
from django.template.defaultfilters import slugify
# Create your models here.




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

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
			self.slug = slugify(self.name)
			super(Category, self).save(*args, **kwargs)
		
	def __unicode__(self):
		return self.name


class Media(models.Model):
	user = models.ForeignKey(User)
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	audio = EmbedVideoField(blank=True)
	artist = models.CharField(max_length=128, blank=True)
	song = models.CharField(max_length=128, blank=True)
	photo = models.ImageField(upload_to='posts', blank=True)
	img_alt =  models.CharField(max_length=128, blank=True)
	quote = models.TextField(blank=True)
	quoter = models.CharField(max_length=128, blank=True)
	updated_at = models.DateTimeField(auto_now=True)
	video = EmbedVideoField(blank=True)


# class AccountManager(BaseUserManager):

# 	def create_user(self, email, password=None, **kwargs):
# 		if not email:
# 			raise ValueError('User must have a valid address.')
# 		if not kwargs.get('username'):
# 			raise ValueError('Users must have a valid username.')

# 		account = self.model( email=self.normalize_email(email), 
# 			username=kwargs.get('username')
# 			)

# 		account.set_password(password)

# 		account.save()

# 		return account 

# 	def create_superuser(self, email, password, **kwargs):
# 		account = self.create_user(email, password, **kwargs)

# 		account.is_admin = True

# 		account.save()

# 		return account


# class Account(AbstractBaseUser):
# 	email = models.EmailField(unique=True)
# 	username = models.CharField(max_length=40, unique=True)
# 	first_name = models.CharField(max_length=40)
# 	last_name = models.CharField(max_length=40)
# 	tagline = models.CharField(max_length=40,blank=True)
# 	is_admin = models.BooleanField(default=False)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)

# 	objects = AccountManager()

# 	USERNAME_FIELD = 'email'
# 	REQUIRED_FIELDS = ['username']

# 	def __unicode__(self):
# 		return self.email

# 	def get_full_name(self):
# 		return ' '.join(self.first_name, self.last_name)

# 	def get_short_name(self):
# 		return self.first_name		



	

# class Page(models.Model):
# 	user = models.ForeignKey(User)
# 	category = models.ForeignKey(Category)
# 	title = models.CharField(max_length=128)
# 	url = models.URLField()
# 	views = models.IntegerField(default=0)
# 	likes = models.IntegerField(default=0)

# 	def __unicode__(self):
# 		return self.title

# class Audio(models.Model):
# 	#This is linking the user ba
# 	user = models.ForeignKey(User)
# 	#This is embeding the music from soundcloud.
# 	audio = EmbedVideoField()
# 	artist = models.CharField(max_length=128)
# 	song = models.CharField(max_length=128)
# 	views = models.IntegerField(default=0)
# 	updated_at = models.DateTimeField(auto_now=True)

# class Photos(models.Model):
# 	user = models.ForeignKey(User)
# 	url = models.URLField()
# 	title = models.CharField(max_length=128)
# 	views = models.IntegerField(default=0)
# 	updated_at = models.DateTimeField(auto_now=True)


# class Quotes(models.Model):
# 	user = models.ForeignKey(User)
# 	url = models.URLField()
# 	quoter = models.CharField(max_length=128)
# 	views = models.IntegerField(default=0)
# 	updated_at = models.DateTimeField(auto_now=True) 


# class Videos(models.Model):
# 	user = models.ForeignKey(User)
# 	video = EmbedVideoField()
# 	title = models.CharField(max_length=128)
# 	views = models.IntegerField(default=0)
# 	updated_at = models.DateTimeField(auto_now=True)


#class Miscellaneous(models.Model):
#	user = models.ForeignKey(User)
#	url = models.URLField()
#	title = models.CharField(max_length=128)
#	views = models.IntegerField(default=0)
#	updated_at = models.DateTimeField(auto_now=True)

