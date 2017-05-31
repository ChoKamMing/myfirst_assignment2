from django.shortcuts import render, redirect
from IPython import embed
from .models import Dojo
# Create your views here.
def index(request):
	
	context = {
		"dojos" : Dojo.objects.all()
	}

	return render(request, 'kris_app/index.html', context)

def dojo_create(request):
	print "in dojo create method"

	postData = {
		"location" : request.POST['location'],
		"state" : request.POST['state']
	}

	model_resp = Dojo.objects.dojo_location_must_not_be_blank_validation(postData)

	print model_resp

	if model_resp[0] == True:
		print "dojo successfully created, I should add a flash message that it was successful"
	else:
		print "It is not successful, please debugging!"
	# if request.POST['location'] == "":
	# 	return redirect('/')
	# else:
	# 	Dojo.objects.create(location=request.POST['location'], state=request.POST['state'])
	return redirect('/')

def form_process(request):
	if request.method == "POST":

  		first_name = request.POST['first_name']
  		last_name = request.POST['last_name']
  		email = request.POST['email']
  	print email
	# print "hello"
	# embed()
	# return render(request, 'kris_app/index.html')
	return redirect("/")

def user_id(request, id):
	if request.session.get(id) ==None:
		requ_sess = None
	else:
		requ_sess = request.session[id]
	# print id
	context = {
		'id' : id,
		'user_info' : request.session[id]
	}
	
	return render(request, 'kris_app/user.html', context)

def user_id_edit(request, id):
	print id
	context = {
		'id' : id,
	}
	return render(request, 'kris_app/edit.html', context)

def user_id_update(request, id):
	print request.POST['kris_secret']

	if request.POST['kris_secret'] == "it_is_secret":
		print "not a secret"
	else:
		print "a secret"
	# print id
	# print request.POST['email']
	# print request.POST['first_name']
	# print request.POST['last_name']
	# print request.POST['occupation']

	# request.session['email'] = request.POST['email']
	# request.session['occupation'] = request.POST['occupation']
	
	request.session[id] = {
		'first_name' : request.POST['first_name'],
		'last_name' : request.POST['last_name'],
		'email' : request.POST['email'],
		'occupation' : request.POST['occupation']
	}

	# print request.session['10']['first_name']
	# print request.session['occupation']

	return redirect("/user_id/"+ id)













