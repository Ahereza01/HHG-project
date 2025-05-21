from django.contrib import admin
#`tywe are accesing the models from the models.py file so that we can administer them to the admin dashboard
from.models import *

# Register your models here.
admin.site.register(Stockx) # Registering the stockx model to the admin dashboard.
admin.site.register(Sale) 
