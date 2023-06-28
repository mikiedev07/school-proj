from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

from .forms import RegisterForm, LoginForm, StudentForm, StudentSearchForm, ProfileUpdateForm, BroadcastForm, SchoolForm, ClassForm
from .models import Student, School, Class
from .utils.send_mail import send_mail


class StudentListView(ListView):
    model = Student
    template_name = 'management/index.html'
    context_object_name = 'students'

    def get_queryset(self):
        queryset = super().get_queryset()
        param = self.request.GET.get('name')

        if param:
            queryset = queryset.filter(Q(name__icontains=param) | Q(class_rel__name__icontains=param))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = StudentSearchForm(self.request.GET)
        return context


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'management/student-create.html'
    success_url = '/'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'management/student-detail.html'
    context_object_name = 'student'


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'management/student-update.html'

    def get_success_url(self):
        s_id = self.kwargs['pk']
        return reverse_lazy('student-detail', kwargs={'pk': s_id})


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = '/'


class SchoolListView(ListView):
    model = School
    template_name = 'management/school-list.html'
    context_object_name = 'schools'


class SchoolCreateView(LoginRequiredMixin, CreateView):
    model = School
    form_class = SchoolForm
    template_name = 'management/school-create.html'
    success_url = '/'


class SchoolDeleteView(LoginRequiredMixin, DeleteView):
    model = School
    success_url = '/'


class ClassListView(ListView):
    model = Class
    template_name = 'management/class-list.html'
    context_object_name = 'classes'


class ClassDeleteView(LoginRequiredMixin, DeleteView):
    model = Class
    success_url = '/'


class ClassCreateView(LoginRequiredMixin, CreateView):
    model = Class
    form_class = ClassForm
    template_name = 'management/class-create.html'
    success_url = '/'


@login_required
def profile(request):
    if request.method == "POST":
        if 'save' in request.POST:
            u_form = ProfileUpdateForm(request.POST, instance=request.user)
            if u_form.is_valid():
                u_form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('profile')
        if 'broadcast' in request.POST:
            b_form = BroadcastForm(request.POST)
            if b_form.is_valid():
                student_emails = Student.objects.values_list('email', flat=True)
                send_mail(list(student_emails), request.POST.get('message'))
                messages.success(request, 'Broadcast done!')
                return redirect('profile')
    else:
        u_form = ProfileUpdateForm(instance=request.user)
        b_form = BroadcastForm()
    context = {
        'u_form': u_form,
        'b_form': b_form
    }

    return render(request, 'management/profile.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Success')
            return render(request, 'management/register.html', {'form': form})
        else:
            errors = form.errors
            return render(request, 'management/register.html', {'form': form, 'errors': errors})
    else:
        form = RegisterForm()
    return render(request, 'management/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            # user = User.objects.get(username=cd['username'])
            # user_check = user.check_password(cd['password'])
            if user:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'management/login.html', {'form': form, 'error': 'Incorrect username or password'})
    else:
        form = LoginForm()
    return render(request, 'management/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')
