from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import NewModel


@login_required
def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('input_text')

        new_model = NewModel()
        new_model.text = temp
        new_model.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        data_list = NewModel.objects.all()
        return render(request,'accountapp/hello_world.html',context={'data_list': data_list})



class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


@method_decorator(login_required('get'))
@method_decorator(login_required('post'))
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'
    form_class = AccountCreationForm
    success_url = reverse_lazy('accountapp:hello_world')


@method_decorator(login_required('get'))
@method_decorator(login_required('post'))
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/delete.html'
    success_url = reverse_lazy('accountapp:hello_world')


