from django.contrib import admin
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.utils.encoding import smart_str
from django.shortcuts import render
from django.urls import path
from django import forms
from .models import UserProfile, AnonymousUser, Room
import csv

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

 
class UserProfileAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def download_csv(self,request,queryset):
        try:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="UserProfiles.csv"'

            writer = csv.writer(response, csv.excel)
            response.write(u'\ufeff'.encode('utf8'))
    
            writer.writerow([
            smart_str(u"User"),
            smart_str(u"Profile Picture"),
            smart_str(u"Phone Number"),
            smart_str(u"Short Description"),
            ])

            for field in queryset:
                writer.writerow([
                    smart_str(field.user),
                    smart_str(field.profile_picture),
                    smart_str(field.phone_number),
                    smart_str(field.short_description),
                ])
            return response
        except Exception as e:
            print(f'ERROR: {e}')
  
    def upload_csv(self, request):
        fields = []
        if request.method == 'POST':
            csv_file = request.FILES['csv_upload']
            file_data = csv_file.read().decode('utf-8')
            csv_data = file_data.split('\n')
            for x in csv_data:
                fields.append(x.split(',')) 

            for field in fields[:4]:
                try:
                    profile = [f for f in field]
                    created = UserProfile.objects.update_or_create(
                            profile_picture = profile[0],
                            phone_number = profile[1],
                            short_description = profile[2],
                            user = User.objects.get(id=profile[3])
                    )
                    print('************REGISTER and/or UPDATE************')
                except Exception as e:
                    print(e)
                finally:
                    fields=[]
                    
        form = CsvImportForm()
        data = {'form': form}
        return render(request, 'admin/accounts/userprofile/csv_upload.html', data)

    list_display = ('user','profile_picture', 'phone_number', 'short_description')
    search_fields = ['user__username', 'phone_number']
    actions = [download_csv]
        

admin.site.register(UserProfile, UserProfileAdmin)

#ANONYMOUSUSER
class AnonymousUserAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'created_date')
    search_fields = ['ip_address', 'created_date']
        
admin.site.register(AnonymousUser, AnonymousUserAdmin)

#ROOMADMIN
class RoomAdmin(admin.ModelAdmin):
    list_display = ('created_date', 'anonymousUser')
    search_fields = ['created_date', 'anonymousUser__ip_address', 'speaker__user__username']
admin.site.register(Room, RoomAdmin)
