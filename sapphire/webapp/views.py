from django.shortcuts import render,HttpResponse

# Create your views here.
def webapp(request):
	return HttpResponse("This is WEBAPP")
