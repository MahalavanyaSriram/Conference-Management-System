from django.contrib import admin
from .models import address, Category, conference, conference_itemTable, skill, comment

# Register your models here.
admin.site.register(address)
admin.site.register(Category)
admin.site.register(conference)
admin.site.register(conference_itemTable)
admin.site.register(skill)
admin.site.register(comment)
