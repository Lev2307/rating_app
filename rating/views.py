from django.shortcuts import render
from django.views import View
from .forms import SimpleForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from .models import Rating

class RatingsListView(ListView):
    model = Rating
    
class SimpleFormView(View):
    form_class = SimpleForm
    initial = {'foo': 'pel`meni'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("")
        
        return render(request, self.template_name, {'form': form})


