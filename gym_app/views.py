from django.shortcuts import render, get_object_or_404, redirect, Http404
from .forms import AddMemberForm
from datetime import datetime
from django.views import View
from .models import Members, SEX


class ShowMembersView(View):
    def get(self, request):
        members = Members.objects.all()
        return render(request, "members.html", {"members":members})

class ShowMembersDetailsView(View):
    def get(self, request, member_id):
        member = Members.objects.get(id = member_id)
        return render(request, "member-details.html", {"member":member, "sex":SEX[int(member.sex)][1]})

class AddMemberView(View):
    def get(self, request):
        form = AddMemberForm()
        return render(request, "member-add.html", {"form":form})

    def post(self, request):
        form = AddMemberForm(request.POST)
        if form.is_valid():
            new_member = Members.objects.create(first_name = form.cleaned_data["first_name"],
                                               last_name = form.cleaned_data["last_name"],
            year_of_birth = form.cleaned_data["year_of_birth"],
            sex = form.cleaned_data["sex"])
            return redirect(f'/member/{new_member.id}')
        return render(request, "member-add.html", {"form":form})
