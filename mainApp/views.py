from django.shortcuts import render
from django.views import View
from .models import Alert
from django.views.generic import TemplateView
from .utils import generate_all_predictions

# Create your views here.
class Index(View):
	def get(self, request):
		alerts = Alert.objects.exclude(enabled=False)
		context = {
			"alerts" : alerts
		}
		return render (request, "index.html", context)
	def post(self, request):
		print("RECIVED POST REQUEST")
		alert_id = request.POST.get('resolveID')
		print("Received request to resolve alert with id " + alert_id)
		return render (request, "index.html", context)

class UploadFiles(TemplateView):
	template_name = "uploadFiles.html"

class Debug(TemplateView):
	template_name = "debug.html"
	def post(self, request):
		generate_all_predictions()
		return render (request, "debug.html", {})