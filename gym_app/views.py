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
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

'''Display main page of application'''
class GymView(View):
    def get(self, request):
        return render(request, "main_page.html")

'''Display gym's members'''
class ShowMembersView(LoginRequiredMixin,PermissionRequiredMixin, View):
    login_url = '/login/'
    permission_required = 'gym_app.view_user'
    def get(self, request):
        users = User.objects.all()
        trainers = Trainers.objects.all()
        users_id = [u.id for u in users]
        trainers_id = [t.user_id for t in trainers]
        members_id = []
        for u in users_id:
            if u not in trainers_id:
                members_id.append(u)
        members = []
        for m_id in members_id:
            user = User.objects.get(id=m_id)
            members.append(user)
        return render(request, "members.html", {"members":members})

'''Display gym's staff'''
class ShowStaffView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        staff = Staff.objects.all()
        return render(request, "staff.html", {"staff":staff})


# class ShowMembersDetailsView(View):
#     def get(self, request, user_id):
#         user = User.objects.get(id = user_id)
#         training_types = TRAININGS
#         return render(request, "user-details.html", {"user":user, "training_types":training_types})

    # def post(self,request,user_id):
    #     user = User.objects.get(id=user_id)
    #     t_type = request.POST.get("t_type")
    #     trainer = Trainers.objects.create(user_id=user_id, training_type=t_type)
    #     return HttpResponse("trainer added")

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

'''Display gym's trainers'''
class ShowTrainersView( View):
    def get(self, request):
        trainers = Trainers.objects.all()
        return render(request, "trainers.html", {"trainers":trainers})

'''Add new staff'''
class AddStaffView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        form = AddStaffForm()
        return render(request, "staff-add.html", {"form":form})

    def post(self, request):
        form = AddStaffForm(request.POST)
        if form.is_valid():
            new_staff = Staff.objects.create(user = form.cleaned_data["user"],
                                               type = form.cleaned_data["type"],
            years_of_experience = form.cleaned_data["years_of_experience"])
            return redirect(f'/staff_details/{new_staff.id}')
        return render(request, "staff-add.html", {"form":form})


'''Display staff details '''
class ShowStaffDetailsView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, id):
        staff = Staff.objects.get(id=id)
        return render(request, "staff-details.html", {"staff": staff})


'''Display training details '''
class ShowTrainingDetailsView(View):
    def get(self, request, id):
        training = Trainings.objects.get(id=id)
        return render(request, "training-details.html", {"training":training})

'''Display avaliable trainings '''
class ShowTrainings(View):
    def get(self, request):
        trainings = Trainings.objects.all()
        traning_list = zip([(str(TRAININGS[int(t.name)][1]))for t in trainings ], [(str(HOURS[int(st.start_time)][1])) for st in trainings],
                           [(str(HOURS[int(et.end_time)][1])) for et in trainings],trainings)
        return render(request, "trainings.html", {"traning_list":traning_list})

'''User login '''
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


'''User logout '''
class Logout(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, request):
        return render(request, "logout.html")

    def post(self, request):
        logout(request)
        return redirect(reverse('main'))

'''Register User (add user) '''
class AddUser(CreateView):
    form_class = AddUserForm
    template_name = "user_add.html"
    success_url = reverse_lazy('main')

'''Add new room '''
class AddRoomView(LoginRequiredMixin, View):
    login_url = '/login/'
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

'''Display all rooms '''
class RoomsView(View):
    def get(self, request):
        rooms = Rooms.objects.all()
        return render(request, "rooms.html", {"rooms":rooms})

'''Add trainer '''
class AddTrainerView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        form = AddTrainerForm()
        user = User.objects.all()
        return render(request, "trainer-add.html", {"form":form, "user":user})

    def post(self, request):
        form = AddTrainerForm(request.POST)
        if form.is_valid():
            trainer = Trainers.objects.create(user = form.cleaned_data["user"],
                                            training_type = form.cleaned_data["training_type"])
            return HttpResponse('''Trainer has been added <br> <a href=''> Back</a> ''')
        return render(request, "main_page.html")

'''Add training '''
class AddTrainingView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        form = AddTrainingForm()
        return render(request, "training-add.html", {"form":form})

    def post(self, request):
        form = AddTrainingForm(request.POST)
        # today = datetime.today().strftime("%Y-%m-%d")
        today = datetime.today()
        trainers = Trainings.objects.all()
        # t_list = [t.trainer.name for t in trainers]

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
                return HttpResponse('''Training has been added <br> <a href='/trainings'> Back</a> ''')
            # return render(request,"training-add.html", {"form":form, "error":"End time before start time"})
        return render(request, "main_page.html")


'''Make reservation '''
class ReservationView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = '/login/'
    permission_required = ('gym_app.add_reservations', 'gym_app.change_reservations', 'gym_app.delete_reservations',
                           'gym_app.view_reservations')
    def get(self, request):
        form = ReservationForm()

        return render(request, "reserve.html", {"form":form})

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
                reservation = Reservations.objects.create(user = request.user,
                                                training = form.cleaned_data["training"],
                                                msg_to_trainer= form.cleaned_data["msg_to_trainer"])
                return HttpResponse('''Reservation has been added <br> <a href='/reserve'> Back</a> ''')
        return render(request, "main_page.html")

'''Display all reservations for currently logged user '''
class UserReservationsView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        if request.user.is_authenticated:
            reservations = Reservations.objects.filter(user_id = request.user.id)
            # trainings_id = [r.training_id for r in reservations]
            # trainings = Trainings.objects.all()
            # trainings_dates = [t.date for t in trainings_id]

            # return render(request, "reservation-details.html", {"reservations": reservations, "trainings":trainings_id, "trainings_dates":trainings_dates})
            return render(request, "reservation-details.html", {"reservations": reservations} )
        else:
            return HttpResponse('''Login error <br> <a href=''> Back</a> ''')
        return redirect(reverse('main'))
    ## this doesnt work when not logged, why ?

