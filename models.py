from django.db import models

class Stock(models.Model):
	ticker = models.CharField(max_length=10)
	def __str__(self):
		return self.ticker

class User(models.Model):
	form = models.CharField(max_length=50)

	# first_name = models.CharField(max_length=50)
	# last_name = models.CharField(max_length=50)
	# email = models.CharField(max_length=50)
	# username = models.CharField(max_length=20)
	# password = models.CharField(max_length=10)

	def __str__(self):
		return self.form
		# return self.last_name 
		# return self.email 
		# return self.mob
		# return self.username 
		# return self.password 


class Ustock(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} - {self.price}"
        return self.ticker








