from django.shortcuts import render
from django.views import View
from .models import Alert
from django.views.generic import TemplateView

# Create your views here.
class Index(View):
	def get(self, request):
		alerts = Alert.objects.exclude(enabled=False)
		context = {
			"alerts" : alerts
		}
		return render (request, "index.html", context)

class UploadFiles(TemplateView):
	template_name = "uploadFiles.html"