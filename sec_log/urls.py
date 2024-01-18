# sec_log/urls.py

from django.urls import path
from .views import event_list, create_event

urlpatterns = [
    path("events/", event_list, name="event_list"),
    path("create_event/", create_event, name="create_event"),
]
