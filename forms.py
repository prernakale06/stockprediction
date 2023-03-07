from django import forms 
from .models import Stock
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class StockForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ["ticker"]
		

# class NewUserForm(UserCreationForm):
# 	# email = forms.EmailField(required=True)
	
# 	class Meta:
# 		model = User 
# 		# fields = ('first_name','last_name','email','username','password1','password2',)
# 		fields = ('first_name','last_name','email','username','password1','password2')

# 		def save(self, commit = True):
# 			user = super(NewUserForm,self).save(commit=False)
# 			if commit:
# 				user.save()
# 				return user

class UstockForm(forms.Form):
	class Meta:
		model = Stock
		fields = ["name","price","quantity","ticker"]

		def save(self, commit=True):
			Stock = super(UstockForm).save(commit=False)
			if commit:
				ustock.save()
				return ustock


	# Do any additional processing of the form data here
		# Save the Ustock instance to the database




