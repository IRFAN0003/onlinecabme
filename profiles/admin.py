from django.contrib import admin
from profiles.models import Driver, NormalUser, Profile


admin.site.register(Profile)
admin.site.register(NormalUser)
admin.site.register(Driver)

