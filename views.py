from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):
	if request.method == 'POST':
		last_name=request.POST['last_name']
		first_name=request.POST['first_name']
		username=request.POST['username']
		password1=request.POST['password1']
		password2=request.POST['password2']
		email=request.POST['email']

		if password1==password2:
			if User.objects.filter(username=username).exists():
				print('username taken')
				messages.error(request,'Username is already taken')
				return render(request,'register.html')
			elif User.objects.filter(email=email).exists():
				print('email taken')
				messages.error(request,'Email is already taken')
				return render(request,'register.html')
			else:
				user= User.objects.create_user(username=username,password=password1,email= email ,first_name=first_name,last_name=last_name)
				user.save();
				print('user created')
				return redirect('login/')
				messages.success(request,'Registration Successful')
		else:
			print("password not match")
			messages.error(request,'Password not matching')
			return render(request, 'register.html')

	else:
		return render(request,'register.html')



	# 	user= User.objects.create_user(username=username,password=password1,email= email ,first_name=first_name,last_name=last_name)
	# 	user.save();
	# 	print('user created')
	# 	return redirect('login/')
	# else:
	# 	return render(request,'register.html')




		
	# 	if password1==password2:
	# 			if User.objects.filter(username=username).exists():
	# 				messages.error(request, "Email number already registered")
	# 				return render(request,'register.html')
	# 			else:
	# 				user= User.objects.create_user(username=username,password=password1,email= email ,first_name=first_name,last_name=last_name)
	# 				user.save()
	# 				messages.success(request, "Your registration is now complete",extra_tags='success')
	# 				return redirect('register.html')
	# 				return render(request,'register.html')
					
	# 	else:
	# 		messages.error(request, "Passwords not matched",extra_tags='error')
	# 		return render(request,'register.html')
	# return render(request,'register.html')

		#user=User.objects.create_user(username=username ,password=password1 ,email= email ,first_name=first_name,last_name=last_name)
		#user.save();
		#print('user created')
		#return redirect('login/')
	#else:
		#return render(request,'register.html')
		#user=User.objects.create_user(username=username ,password=password1 ,email= email ,first_name=first_name,last_name=last_name)
		#user.save();
		#print('user created')
		#return redirect('login/')
	#else:
		#return render(request,'register.html')

# def login(request):
# 	if request.method=="POST":
# 		first_name=request.POST.get('first_name')
# 		last_name=request.POST.get('last_name')
# 		username=request.POST.get('username')
# 		email=request.POST.get('email')
# 		password1= request.POST.get('password1')
# 		password2= request.POST.get('password2')

# 		if password1==password:
# 			if User.objects.filter(username=username).exists():
# 				messages.error(request, "Email number already registered")
# 			else:
# 				user= User.objects.create_user(username=username,password1=password)
# 				user.save()
# 				messages.success(request, "Your registration is now complete",extra_tags='success')
# 				return render(request,'register.html')
# 		else:
# 			messages.error(request, "Passwords not matched",extra_tags='error')
# 			return render(request,'register.html')
# 		return render(request,'register.html')
	