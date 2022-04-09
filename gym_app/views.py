from django.shortcuts import render, get_object_or_404, redirect, Http404
from .forms import AddMemberForm, AddStaffForm, LoginForm, AddUserForm, AddRoomForm, AddTrainerForm
from datetime import datetime
from django.views import View
from .models import Members, SEX, Staff, Trainings, TRAININGS, TYPES, Rooms
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

class GymView(View):
    def get(self, request):
        return render(request, "main_page.html")


class ShowMembersView(LoginRequiredMixin, View):
    def get(self, request):
        members = User.objects.all()
        return render(request, "members.html", {"members":members})

class ShowMembersDetailsView(View):
    def get(self, request, user_id):
        user = User.objects.get(id = user_id)
        return render(request, "user-details.html", {"user":user})

# class AddMemberView(View):
#     def get(self, request):
#         form = AddMemberForm()
#         return render(request, "member-add.html", {"form":form})
#
#     def post(self, request):
#         form = AddMemberForm(request.POST)
#         if form.is_valid():
#             new_member = Members.objects.create(first_name = form.cleaned_data["first_name"],
#                                                last_name = form.cleaned_data["last_name"],
#             year_of_birth = form.cleaned_data["year_of_birth"],
#             sex = form.cleaned_data["sex"])
#             return redirect(f'/member/{new_member.id}')
#         return render(request, "member-add.html", {"form":form})

class ShowTrainersView( View):
    def get(self, request):
        trainers = Staff.objects.filter(type=0)
        trainings = Trainings.objects.all()
        trainers_ids = [trainer.id for trainer in trainers]
        trainings_names = [[TRAININGS[int(t)][1]] for t in trainers_ids]

        return render(request, "trainers.html", {"trainers":trainers})

class AddStaffView(View):
    def get(self, request):
        form = AddStaffForm()
        return render(request, "staff-add.html", {"form":form})

    def post(self, request):
        form = AddStaffForm(request.POST)
        if form.is_valid():
            new_staff = Staff.objects.create(first_name = form.cleaned_data["first_name"],
                                               last_name = form.cleaned_data["last_name"],
            year_of_birth = form.cleaned_data["year_of_birth"],
            type = form.cleaned_data["type"])
            return redirect(f'/staff_details/{new_staff.id}')
        return render(request, "staff-add.html", {"form":form})



class ShowStaffDetailsView(View):
    def get(self, request, id):
        staff = Staff.objects.get(id=id)
        training_type = (TRAININGS[int(staff.type)])[1]
        return render(request, "staff-details.html", {"staff": staff, "training_type":training_type})

class ShowTrainings(View):
    def get(self, request):
        trainings = Trainings.objects.all()
        trainings_names = []
        for t in trainings:
            trainings_names.append(t.name)
        intigers = []
        for i in trainings_names:
            intigers.append(int(i))
        names = []
        for j in intigers:
            names.append(TRAININGS[j])
        names_list = []
        for n in names:
            names_list.append(n[1])

        zipped_list = zip(trainings, names_list)
        return render(request, "trainings.html", {"zipped":zipped_list})


class Login(FormView):
    form_class = LoginForm
    template_name = "login_form.html"

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data["login"],
                            password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
        else:
            return HttpResponse('''Login error <br> <a href=''> Back</a> ''')
        return redirect(reverse('main'))



class Logout(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, "logout.html")

    def post(self, request):
        logout(request)
        return redirect(reverse('main'))


class AddUser(CreateView):
    form_class = AddUserForm
    template_name = "user_add.html"
    success_url = reverse_lazy('main')


class Reservation(View):
    def get(self, request):
        return render(request, "logout.html")

class AddRoomView(View):
    def get(self, request):
        form = AddRoomForm()
        return render(request, "room-add.html", {"form":form})

    def post(self, request):
        form = AddRoomForm(request.POST)
        if form.is_valid():
            new_room = Rooms.objects.create(name = form.cleaned_data["name"],
                                            capacity = form.cleaned_data["capacity"],
                                            training=form.cleaned_data["training"])
            return redirect(f'/room/{new_room.id}')
        return render(request, "room-add.html", {"form":form})

class RoomsView(View):
    def get(self, request):
        rooms = Rooms.objects.all()
        return render(request, "rooms.html", {"rooms":rooms})


class AddTrainerView(View):
    def get(self, request):
        form = AddTrainerForm()
        user = User.objects.all()
        return render(request, "trainer-add.html", {"form":form, "user":user})

    def post(self, request):
        form = AddTrainerForm(request.POST)
        if form.is_valid():
            trainer = Trainers.objects.create(user = form.cleaned_data["user"],
                                            training_type = form.cleaned_data["training_type"])
            return redirect(f'/room/{new_room.id}')
        return render(request, "room-add.html", {"form":form})