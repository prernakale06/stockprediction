from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import logging
from .forms import UstockForm
from .forms import User
from .forms import Stock
import requests
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)



def home(request):
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		#pk_ac36394439654e409b7e91cd48bb66f9
		#pk_9c2a3ec49ae2485f81efc674fbb93b84
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token=pk_9c2a3ec49ae2485f81efc674fbb93b84")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error"
		return render(request, "home.html", {'api': api})
		
	else:
		return render(request, "home.html", {'api':"Enter a Ticker Symbol Above... "})
		

	

def about(request):
	return render(request, "about.html", {})

def add_stock(request):
	import requests
	import json

	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ('Stock Has Been Added!'))
			return redirect('add_stock')
	else:
		ticker = Stock.objects.all()
		output = []
		for ticker_item in ticker:
			logger.info(ticker_item)
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+str(ticker_item)+"/quote?token=pk_f812e7d053754a82b80482da14d7d104")
			logger.info(api_request)
			try:
				api = json.loads(api_request.content)
				output.append(api)
				print(output)
			except Exception as e:
				api = "Error"
			

		return render(request, "add_stock.html", {'ticker': ticker,'output':output})
		
def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request,("Stock Has Been Deleted!"))
	return redirect(delete_stock)

def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request, 'delete_stock.html', {'ticker':ticker})


# def register(request, methods=('GET','POST')):
# 	if request.method == "POST":
# 		#print(request.form)
# 		last_name=request.POST.get('last_name')
# 		first_name=request.POST.get('first_name')
# 		username=request.POST.get('username')
# 		password1=request.POST.get('password1')
# 		password2=request.POST.get('password2')
# 		email=request.POST.get('email')
		
# 		if password1==password2:
# 				if User.objects.filter(username=username).exists():
# 					messages.error(request, "Email number already registered")
# 					return render(request,'register.html')
# 				else:
# 					user= User.objects.create_user(username=username,password=password1,email= email ,first_name=first_name,last_name=last_name)
# 					user.save()
# 					messages.success(request, "Your registration is now complete",extra_tags='success')
# 					# return redirect('register.html')
# 					return render(request,'register.html')
					
# 		else:
# 			messages.error(request, "Passwords not matched",extra_tags='error')
# 			return render(request,'register.html')


def login(request):
	import requests
	import json
	if request.method=="POST":
		#email=request.POST.get('email') 
		password1=request.POST.get('password')
		username=request.POST['username']

		user = auth.authenticate(username=username,password=password1)

		if user is not None:
			auth.login(request, user)
			return redirect('register.html')
		else:
			messages.error(request,"Username or password entered",extra_tags='error')
			return render(request,'login.html')

	return render(request,'login.html')

def logout(request):
	auth.logout(request)
	return redirect('login.html')

def main(request):
	return render(request,'main.html')

def contact(request):
	return render(request,'contact.html')

def Addition(num1,num2):
    result = int(num1) + int(num2)
    return result
def Subtraction(num1,num2):
	result = int(num1) - int(num2)
	return result

def Multiplication(num1,num2):
	result = int(num1) * int(num2)
	return result

def Divide(num1,num2):
	result=int(num1)/int(num2)
	return result

def calculator(request):
	if request.method == 'POST':
	   	num1 = request.POST['num1']
	   	num2 = request.POST['num2']
	   	if 'add' in request.POST:
	   		result = Addition(num1,num2)
	   		return render(request,'calculator.html',{'result':result})
	   	if 'sub' in request.POST:
	   		result = Subtraction(num1,num2)
	   		return render(request,'calculator.html',{'result':result})
	   	if 'div' in request.POST:
	   		result = Divide(num1,num2)
	   		return render(request,'calculator.html',{'result':result})
	   	if 'mul' in request.POST:
	   		result = Multiplication(num1,num2)
	   		return render(request,'calculator.html',{'result':result})
	return render (request,'calculator.html')

def ustock(request):
	if request =="POST":
		name=request.POST.get("name")
		price=request.POST.get("price")
		date=request.POST.get("date")

		# ticker = Stock.objects.all()
		# output = []
		# output.append(api)
		# print(output)

	return render(request,'ustock.html')