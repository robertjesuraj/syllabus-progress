from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.db.models import Count

from django.urls import reverse_lazy
# Create your views here.
from .models import Syllabus
from .forms import MyModelForm

class IndexView(generic.ListView):
    template_name = 'kichu/index.html'
    # context_object_name = 'syllabus_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        # return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        return Syllabus.objects.all()


class SyllabusList(generic.ListView):
    model = Syllabus
    # def get_queryset(self):
    #     return Syllabus.objects.values('proposed_date_completeion').annotate(dcount=Count('proposed_date_completeion'))

class SyllabusCreate(generic.edit.CreateView):
    model = Syllabus
    fields = ['syllabus_text', 'proposed_date_completeion', 'completion_status']
    # fields = ['syllabus_text']
    # forms = MyForm()
    forms = MyModelForm()
    success_url = reverse_lazy('kichu:syllabus_list')


class SyllabusUpdate(generic.edit.UpdateView):
    model = Syllabus
    fields = ['syllabus_text', 'proposed_date_completeion', 'completion_status']
    # fields = ['syllabus_text']
    forms = MyModelForm()
    success_url = reverse_lazy('kichu:syllabus_list')


class SyllabusDelete(generic.edit.DeleteView):
    model = Syllabus
    success_url = reverse_lazy('kichu:syllabus_list')