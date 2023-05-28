from django.urls import path
from . import views

urlpatterns = [
    path('rest/v1/calendar/init/', views.google_calendar_init_view, name='calendar-init'),
    path('rest/v1/calendar/redirect/', views.google_calendar_redirect_view, name='calendar-redirect'),
]

