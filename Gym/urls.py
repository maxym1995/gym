"""Gym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gym_app.views import   (ShowMembersView, ShowTrainersView, AddStaffView,
                            ShowStaffDetailsView, ShowTrainings, Login, Logout, AddUser, GymView,
                            AddRoomView, RoomsView, AddTrainerView, AddTrainingView, ReservationView, ShowTrainingDetailsView,
                            UserReservationsView, ShowStaffView
                            )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", GymView.as_view(), name = "main"),
    path("rooms/", RoomsView.as_view(), name = "rooms"),
    path("trainers/", ShowTrainersView.as_view(), name = "trainers"),
    path("staff_add/", AddStaffView.as_view(), name = "staff-add"),
    path("staff_details/<int:id>/", ShowStaffDetailsView.as_view(), name = "staff-details"),
    path("trainings/", ShowTrainings.as_view(), name="trainings"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('add_user/', AddUser.as_view(), name="add-user"),
    path('room_add/', AddRoomView.as_view(), name="room-add"),
    path('trainer_add/', AddTrainerView.as_view(), name="trainer-add"),
    path('training_add/', AddTrainingView.as_view(), name="training-add"),
    path('reserve/', ReservationView.as_view(), name="reserve"),
    path("training_details/<int:id>/", ShowTrainingDetailsView.as_view(), name = "training-details"),
    path("reservation_details/", UserReservationsView.as_view(), name = "reservation-details"),
    path("staff/", ShowStaffView.as_view(), name = "staff"),
    path("members/", ShowMembersView.as_view(), name = "members"),
    # path("member_details/<int:user_id>/", ShowMembersDetailsView.as_view(), name = "member-details"),
    # path("member_add/", AddMemberView.as_view(), name = "member-add"),

]
