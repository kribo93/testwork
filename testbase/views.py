from testbase.models import Student, Group
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.utils.http import is_safe_url
from django.contrib.messages.views import SuccessMessageMixin



class MyLoginView(LoginView):
    template_name = 'testbase/login.html'
    default_redirect_to = '/'
    success_url = '/'

    def get_success_url(self):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to

class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'testbase/group_list.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super(GroupListView, self).get_context_data(**kwargs)
        context['group'] = Group
        return context


class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'testbase/group_detail.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['student'] = Student
        context['students_list'] = Student.objects.filter(in_group=self.kwargs['pk'])
        return context

class GroupCreateView(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    model = Group
    template_name = 'testbase/group_create.html'
    login_url = '/login/'
    success_message = "Group was created successfully"
    fields = ('name', 'course_leader',)
    success_url = '/'


    def form_valid(self, form):
        form.save()
        return super(GroupCreateView, self).form_valid(form)


class GroupUpdateView(SuccessMessageMixin,LoginRequiredMixin, UpdateView):
    model = Group
    template_name = 'testbase/group_edit.html'
    login_url = '/login/'
    success_message = "Group was updated successfully"
    success_url = '/'
    fields = ('name', 'course_leader',)

class GroupDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'testbase/group_delete.html'
    login_url = '/login/'
    success_message = "Group was deleted successfully"
    success_url = '/'


class StudentCreateView(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'testbase/student_create.html'
    login_url = '/login/'
    success_message = "Student was created successfully"
    fields = ('first_name', 'last_name', 'date_of_birth', 'card_number', 'in_group',)
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(SuccessMessageMixin,LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'testbase/student_update.html'
    login_url = '/login/'
    success_message = "Student was updated successfully"
    success_url = '/'
    fields = ('first_name', 'last_name', 'date_of_birth', 'card_number', 'in_group',)

class StudentDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'testbase/student_delete.html'
    login_url = '/login/'
    success_message = "Student was deleted successfully"
    success_url = '/'
