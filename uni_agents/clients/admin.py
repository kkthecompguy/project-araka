from django.contrib import admin
from .models import University, Agent

# Register your models here.
admin.site.register(University)
admin.site.register(Agent)

# customizing site
admin.site.site_header = 'Explore Education Africa System'
admin.site.site_title = 'Welcome'
admin.site.index_title = 'Explore Education Africa'