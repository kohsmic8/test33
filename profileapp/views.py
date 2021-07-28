
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
        model = Profile
        form_class = ProfileCreationForm
        success_url = reverse_lazy('accountapp:hello_world')
        template_name = 'profileapp/create.html'

        def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)
            # forms와 models의 필드값중 user이 매칭이 안되어 오류가 발생하므로 처리하는 작업(오버라이딩)

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'