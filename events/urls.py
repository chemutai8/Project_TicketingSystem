from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventListView.as_view(), name='event-list'),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('event/new/', views.EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/purchase/', views.purchase_ticket, name='purchase-ticket'),
    path('my-tickets/', views.my_tickets, name='my-tickets'),
    path('ticket/<int:ticket_id>/cancel/', views.cancel_ticket, name='cancel-ticket'),
]