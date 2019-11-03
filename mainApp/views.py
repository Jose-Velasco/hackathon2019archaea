from django.shortcuts import render
from django.views import View
from .models import Alert
from django.views.generic import TemplateView
from .utils import disable_alert

from .forms import ResolveForm

# Create your views here.
class Index(View):
	form_class = ResolveForm
	intial = {'resolveID' : 0}
	template_name = 'index.html'

	def get(self, request, *args, **kwargs):
		print("INDEX.GET")
		alerts = Alert.objects.exclude(enabled=False)
		context = {
			"alerts" : alerts,
			'form' : self.form_class()
		}
		return render (request, self.template_name, context)
	def post(self, request, *args, **kwargs):
		print("INDEX.POST")
		form = self.form_class(request.POST)
		
		if form.is_valid():
			print("Form is valid!")
			alert_id = form.cleaned_data['resolveID']
			print("Received request to resolve alert with id " + str(alert_id))
			disable_alert(1)
		else:
			print("Form is not valid!")

		context = {
			'alerts' : Alert.objects.exclude(enabled=False),
			'form' : form
		}
		return render (request, self.template_name, context)

class UploadFiles(TemplateView):
	template_name = "uploadFiles.html"

class Debug(TemplateView):
	template_name = "debug.html"
	def post(self, request):
		#generate_all_predictions()
		return render (request, "debug.html", {})