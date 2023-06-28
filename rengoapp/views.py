from django.shortcuts import render
from .models import Report,Planet,Comp
from django.views import generic
from django.views.generic import CreateView, TemplateView,ListView,DeleteView,DetailView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from rengoapp.forms import FarmForm,AddReportForm
from django.core.exceptions import PermissionDenied




class SignView(generic.TemplateView):
    template_name = 'sign.html'
    model =Report
# Create your views here.
class HomeView(ListView):
    template_name = 'home.html'
    model=Planet

class CreateCustomerView(LoginRequiredMixin,CreateView):
    model = Planet
    fields=('name','planet')
    template_name = 'create/create_customer.html'

    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user =self.request.user

        return super().form_valid(form)

class FarmMenuView(LoginRequiredMixin,DetailView):
    template_name = 'menu/farm-menu.html'
    model=Planet



def reportlist_view(request,user):
    report_list = Report.objects.filter(user_id=user).order_by('id')
    users=Planet.objects.order_by('id')

    return render(request,'menu/report-list.html', {'object_list': report_list, 'object': users},)

def report_detail_view(request):
    report_list = Report.objects.order_by('id')
    

    return render(request,'report-detail.html', {'item': report_list},)

class DetailPlaceView(generic.DetailView):
    template_name = 'report-detail.html'
    model = Report

#新規作業報告書　作成
class CreateReportView(LoginRequiredMixin,CreateView):
    model = Report
    form_class=AddReportForm
    template_name = 'create/create_report.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_report_form'] = AddReportForm    #ここで定義した変数名
        return context
    def form_valid(self, form):
       qryset =  form.save(commit=False)
       qryset.writer=self.request.user
       qryset.save()
       print(qryset)
        
       return super().form_valid(form)

    
class DeleteReportView(LoginRequiredMixin,DeleteView):
    model = Report
    template_name = 'report/delete.html'
    
    success_url=reverse_lazy('home')
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj     
      

class UpdateReportView(LoginRequiredMixin,UpdateView):
    model = Report
    fields=AddReportForm
    template_name = 'report/update.html'
    success_url=reverse_lazy('home')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj       
    #def get_success_url(self):
    #    return reverse('detail-report' , kwargs={'pk':self.object.id})

    
