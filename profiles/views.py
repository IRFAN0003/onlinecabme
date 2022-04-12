from multiprocessing import context
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView,UpdateView
from django.views import View
from django.contrib.auth import authenticate,login,logout, get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from profiles.forms import UserLoginForm, UserRegistrationForm
from profiles.models import Driver, NormalUser, Profile

User = get_user_model()

class UserRegisterView(View):
    template_name = 'registration/register.html'
    form_class = UserRegistrationForm

    def get(self, request):
        context = {
            'form' : self.form_class()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        is_driver = request.POST.get('is_driver')
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create()
        else:
            context = {
                'form' : form
            }
            return render(request, self.template_name, context)

        if is_driver:
            driver = Driver.objects.create(
                user = user,
                profile = profile,
            )

        else:
            normal_user = NormalUser.objects.create(
                user = user,
                profile = profile
            )

        return redirect('login')


class UserLoginView(View):
    template_name = 'registration/login.html'
    form_class = UserLoginForm

    def get(self, request):
        context = {
            'form' : self.form_class()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return self.get_success_url(user)
        context = {
            'form' :self.form_class(request)
        }
        return render(request, self.template_name, context)


    def get_success_url(self, user):
        url = 'dashboard'
        driver = Driver.objects.filter(user_id=user.id).first()
        if driver:
            url = 'dashboard_driver'
        return redirect(reverse_lazy(url))


class DashboardView(TemplateView):
    template_name = 'profiles/dashboard.html'
    


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profiles/profile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = Profile.objects.get(normaluser__user__id=self.request.user.id)
        context['userprofile'] = user_profile
        return context


class UserProfileUpdateView(UpdateView):
    template_name = 'profiles/update_profile.html'
    model = User
    fields = ['username','password','email'] 
    success_url = '/accounts/profile/'





