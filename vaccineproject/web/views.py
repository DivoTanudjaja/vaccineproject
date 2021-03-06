from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SignUpForm
from django.urls import reverse

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

class SignUpView(TemplateView):
    template_name = 'adduser.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            return render(request, self.template_name, {'form':form})
