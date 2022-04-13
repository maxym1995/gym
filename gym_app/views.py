from django.shortcuts import render, get_object_or_404, redirect, Http404
from .forms import AddMemberForm, AddStaffForm, LoginForm, AddUserForm, AddRoomForm, AddTrainerForm, AddTrainingForm, ReservationForm
from datetime import datetime
from django.views import View
from .models import Members, SEX, Staff, Trainings, TRAININGS, TYPES, Rooms, Trainers, Reservations, HOURS
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

class ShowStaffView(LoginRequiredMixin, View):
    def get(self, request):
        staff = Staff.objects.all()
        return render(request, "members.html", {"members":members})

class ShowMembersDetailsView(View):
    def get(self, request, user_id):
        user = User.objects.get(id = user_id)
        training_types = TRAININGS
        return render(request, "user-details.html", {"user":user, "training_types":training_types})

    def post(self,request,user_id):
        user = User.objects.get(id=user_id)

        t_type = request.POST.get("t_type")
        trainer = Trainers.objects.create(user_id=user_id, training_type=t_type)
        return HttpResponse("trainer added")

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
        traning_list = zip([(str(TRAININGS[int(t.name)][1]))for t in trainings ], [(str(HOURS[int(st.start_time)][1])) for st in trainings],
                           [(str(HOURS[int(et.end_time)][1])) for et in trainings],trainings)
        return render(request, "trainings.html", {"traning_list":traning_list})


class ShowTrainingDetailsView(View):
    def get(self, request, id):
        training = Trainings.objects.get(id=id)
        return render(request, "training-details.html", {"training":training})

class ShowTrainings(View):
    def get(self, request):
        trainings = Trainings.objects.all()
        traning_list = zip([(str(TRAININGS[int(t.name)][1]))for t in trainings ], [(str(HOURS[int(st.start_time)][1])) for st in trainings],
                           [(str(HOURS[int(et.end_time)][1])) for et in trainings],trainings)
        return render(request, "trainings.html", {"traning_list":traning_list})


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
            return HttpResponse("Trainer has been added")
        return render(request, "main_page.html")


class AddTrainingView(View):
    def get(self, request):
        form = AddTrainingForm()
        return render(request, "training-add.html", {"form":form})

    def post(self, request):
        form = AddTrainingForm(request.POST)
        # today = datetime.today().strftime("%Y-%m-%d")
        today = datetime.today()
        trainers = Trainings.objects.all()
        t_list = [t.trainer.name for t in trainers]

        if form.is_valid():
            if form.cleaned_data["start_time"] > form.cleaned_data["end_time"]:
                return render(request, "training-add.html", {"form":form, "error":"End time before start time"})
            # if form.cleaned_data["trainer"] in t_list:
            #     return render(request, "training-add.html", {"form":form, "error":"This trainer is already assigned to training."})
            else:
                training = Trainings.objects.create(name = form.cleaned_data["name"],
                                                trainer = form.cleaned_data["trainer"],
                                                start_time=form.cleaned_data["start_time"],
                                                end_time=form.cleaned_data["end_time"],
                                                date=form.cleaned_data["date"],
                                                max_participants=form.cleaned_data["max_participants"])
                return HttpResponse("Training has been added")
            # return render(request,"training-add.html", {"form":form, "error":"End time before start time"})
        return render(request, "main_page.html")


class ReservationView(LoginRequiredMixin, View):
    def get(self, request):
        form = ReservationForm()
        return render(request, "reserve.html", {"form":form})

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
                reservation = Reservations.objects.create(user = form.cleaned_data["user"],
                                                training = form.cleaned_data["training"],
                                                msg_to_trainer= form.cleaned_data["msg_to_trainer"])
                return HttpResponse("Reservation has been added")
        return render(request, "main_page.html")


