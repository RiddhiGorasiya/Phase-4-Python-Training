from django.contrib import admin
from student.models import Profile, Result

# Register your models here.

# admin.site.register(Profile)
# admin.site.register(Result)

# create model admin class
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'email', 'city') # id is default generate password

admin.site.register(Profile, ProfileAdmin)

class ResultAdmin(admin.ModelAdmin):
    list_display = ('stu_class', 'marks')

admin.site.register(Result, ResultAdmin)

# @admin.register(Profile) # another way use to admin class model
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'roll', 'email', 'city') # id is default generate password
