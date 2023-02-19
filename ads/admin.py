from django.contrib import admin

from ads.models import Ads, Category, Location, User

admin.site.register(Ads)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Location)
