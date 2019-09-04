from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import   Company

@login_required
def home(request):
    context = {
        'posts': Company.objects.all()
    }
    return render(request, 'companies/home.html', context)


class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'companies/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'companies'
    paginate_by = 5


class CompanyDetailView(DetailView):
    model = Company


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    fields = ['name', 'email', 'logo', 'website']

    def form_valid(self, form):
        return super().form_valid(form)


class CompanyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Company
    fields = ['name', 'email', 'logo', 'website']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        companies = self.get_object()
        return  True


class CompanyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Company
    success_url = '/'

    def test_func(self):
        company = self.get_object()
        return  True