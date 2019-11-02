from django.shortcuts import render
from django.views import View
from .models import Alert

# Create your views here.
class Index(View):
	def get(self, request):
		alerts = Alert.objects.exclude(enabled=False)
		context = {
			"alerts" : alerts
		}
		return render (request, "index.html", context)