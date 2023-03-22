from django.shortcuts import render,redirect
from companyapp.models import companydata
from companyapp.forms import companyform

def homepage(request):
	return render(request, 'apps/home.html')


def about(request):
	return render(request, 'apps/about.html')

def services(request):
	return render(request, 'apps/services.html')

def blog(request):
	return render(request, 'apps/blog.html')

def contact(request):
	form=companyform()
	if request.method=='POST':
		form= companyform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/home')

	return render(request, 'apps/contact.html',{'form':form})
