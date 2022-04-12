
from django.urls import path, include
from profiles.views import (
    DashboardView, UserLoginView, UserProfileView, UserRegisterView,UserProfileUpdateView
    )


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('user/login/',UserLoginView.as_view(),name='login'),
    path('register/',UserRegisterView.as_view(),name='register'),
    path('dashboard/',DashboardView.as_view(),name='dashboard'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('update/<int:pk>/',UserProfileUpdateView.as_view(),name='profile_update'),
    
    

]