from django.shortcuts import render
from django.views.generic import TemplateView,View
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

class HomeView(TemplateView):
    template_name = 'general/home.html'


class AboutView(TemplateView):
    template_name = 'general/about.html'
    success_url = '/general/about'

class ContactView(View):
    template_name ='general/contact_us.html'
    def get(self,request):
        return render(request,self.template_name)

    

    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        email_from = settings.EMAIL_HOST_USER
        subject = f'feedback from {name}'
        send_mail(subject,message,email_from,[email])
        messages.success(request,'send successfully',extra_tags='alert-sucess')
        return render(request,self.template_name)





