from django.contrib import admin
from .models import UserProfile


#customisation admin side
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','user_info','phone','url')# display this data admin side 

    def user_info(self,obj):# change name 'description' with 'user_info' admin side
        return obj.description

    def get_queryset(self,request):
        queryset = super(UserProfileAdmin,self).get_queryset(request)
        queryset = queryset.order_by('phone') # apply '-phone' display reverse order(descending)
        return queryset  # display phone number order by admin side(aescending)
        
    user_info.short_description = 'Info' # change name user_info to info 

# registerd userprofile model in admin side
admin.site.register(UserProfile, UserProfileAdmin)

# admin.site.site_header= 'Administration' # change admin side header title