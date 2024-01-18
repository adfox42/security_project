# sec_log/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import EventForm
from .models import Event


def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "event_list"
            )  # Redirect to the event list page after saving
    else:
        form = EventForm()

    return render(request, "sec_log/create_event.html", {"form": form})


def event_list(request):
    user_id = request.GET.get("user_id")  # Get the user ID from query parameters
    events = Event.objects.all().order_by(
        "-timestamp"
    )  # Default sorting chronologically

    if user_id:
        events = events.filter(user__id=user_id)  # Filter events by selected user

    users = User.objects.all().order_by(
        "first_name"
    )  # Get all users, sorted by first name
    return render(
        request, "sec_log/event_list.html", {"events": events, "users": users}
    )
