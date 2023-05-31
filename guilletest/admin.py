from django.contrib import admin
from .models import User
from .models import TextInputs
from .models import ScrapingCounter

# Register your models here.
admin.site.register(User)
admin.site.register(TextInputs)
admin.site.register(ScrapingCounter)