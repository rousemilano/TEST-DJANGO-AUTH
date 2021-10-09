from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserProfile, AnonymousUser
from .forms import UsersForm, UserProfileForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
import socket

def home(request):
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        anonymous= AnonymousUser(ip_address=ip)   
        anonymous.save()
        print('*****************REGISTER ANONYMOUS*********************')
    except Exception as e:
        print(f'ERROR: {e}')

    return render(request, 'home.html')


class RegisterUser(CreateView):
    model = UserProfile
    template_name = "user/user_register.html"
    form_class =  UserProfileForm
    second_form_class = UsersForm
    success_url = reverse_lazy('login')
    
    def get_context_data(self, **kwargs):
        context = super(RegisterUser, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request,*args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST,request.FILES)
        form2 = self.second_form_class(request.POST,request.FILES)
    
        if form.is_valid() and form2.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = form2.save()
            user_profile.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))



