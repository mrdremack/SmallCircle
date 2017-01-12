from django import forms
from models import Media, Category, UserProfile
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.utils.crypto import get_random_string


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website','picture', 'bio')


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username','email','password')


class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text='Please enter a category name!')
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
			model = Category
			fields = ('name',)
			exclude = ('user',)

class MediaForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text='Please enter a page title!')
	url = forms.URLField(max_length=200, help_text='Please enter page URL!')
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')

		if url and not url.startswith('http://'):
			url = 'http://' + url
			cleaned_data['url'] = url
		return cleaned_data

	class Meta:
			model = Media
			exclude = ('category', 'user')

class ContactForm(forms.Form):
	name = forms.CharField(required=True)
	email = forms.CharField(widget=forms.EmailInput(),required=True)
	subject = forms.CharField(required=True)
	body = forms.CharField(widget=forms.Textarea(),required=True)

	def send_message(self):
		name = self.cleaned_data['name']
		email = self.cleaned_data['email']
		subject = self.cleaned_data['subject']
		body = self.cleaned_data['body']

		message = '''
				New Message from {name} @ {email}
				Subject: {subject}
				Message:
				{body}
				'''.format(name=name,
					email=email,
					subject=subject,
					body=body)

		email_msg = EmailMessage('New Contact form Submission',
			message,
			email,
			['mr.dremack@gmail.com'])

		email_msg.send()

class PasswordRecoveryForm(forms.Form):
	email = forms.EmailField(required=False)

	def clean_email(self):
		try:
			return User.objects.get(email=self.cleaned_data['email'])
		except User.DoesNotExist:
			raise forms.ValidationError("Can't find a user based on this email")
		return self.cleaned_data['email']

	def reset_password(self):
		user = self.cleaned_data['email']

		password = get_random_string(length=8)

		user.set_password(password)

		user.save()

		body = """
				Sorry you are having issues with your account.  Below is your username and new password:

				Username: {username}
				Password:{password}

				You can log in here: http://localhost:800/login/
				You can change your password here: http://localhost/settings/

				""".format(username=user.username, password=password)


		pw_msg = EmailMEssage('Your new password', body, 'mr.dremack@gmail.com', [user.email])

		pw_msg.send()