
from django.http import HttpResponse
from datetime import datetime

def myFunc(request):
	x = datetime.today()
	return HttpResponse(x)