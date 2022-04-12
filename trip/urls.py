from django.urls import path, include

from trip.views import TripsCreateView, TripsListView,TripsUpdateView,TripsDetailsView,TripsDeleteView

urlpatterns = [
    path('',TripsListView.as_view(),name='trip'),
    path('trip/create/',TripsCreateView.as_view(),name='trip_create'),
    path('trip/details/<int:pk>/',TripsDetailsView.as_view(),name='details'),
    path('trip/update/<int:pk>/',TripsUpdateView.as_view(),name='update'),
    path('trip/delete/<int:pk>/',TripsDeleteView.as_view(),name='delete'),


]