from django.urls import path

from driver.views import DriverDashboardView

urlpatterns =[

    path('dashboard/', DriverDashboardView.as_view(), name='dashboard_driver')

]