from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import  Employee

@login_required
def home(request):
    context = {
        'posts': Employee.objects.all()
    }
    return render(request, 'employees/home.html', context)


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employees/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'employees'
    paginate_by = 5


class EmployeeDetailView(DetailView):
    model = Employee


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    fields = ['first_name', 'last_name', 'email', 'phone', 'company']

    def form_valid(self, form):
        return super().form_valid(form)


class EmployeeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Employee
    fields = ['first_name', 'last_name', 'email', 'phone', 'company']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        employees = self.get_object()
        return  True


class EmployeeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Employee
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return True
