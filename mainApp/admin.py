from django.contrib import admin
from . import models
models_to_register = [models.Neighborhood, models.Location, models.Issue, models.Date, models.Alert]
admin.site.register(models_to_register)