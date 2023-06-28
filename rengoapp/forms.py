from django import forms
from .models import Report
from django.utils import timezone


##日付入力
class DateInput(forms.DateInput):
    input_type = 'date'

class DateTimeInput(forms.DateInput):
    input_type = 'datetime'

class FarmForm(forms.Form):
     user = forms.CharField()
     planet = forms.CharField() 


class ReportForm(forms.Form):
     user= forms.CharField()
     writer= forms.CharField()
     write_date = forms.DateField()
     work_time_s=forms.DateTimeField()
     work_time_f=forms.DateTimeField()
     work_content=forms.CharField(widget=forms.Textarea) 


class AddReportForm(forms.ModelForm):
     class Meta:
          model=Report
          fields=('worker','write_date','work_time_s','work_time_f','work_content','user')
          labels = {'worker':'作業員', 'write_date':'記入日', 'work_time_s':'作業開始時間', 'work_time_f':'作業終了時間', 'work_content':'作業内容', 'user':'お客様'}
          widgets={
          'write_date':DateInput(),
          'work_time_f':DateTimeInput(attrs={"type": "datetime-local", "value": timezone.datetime.now().strftime('%Y-%m-%dT%H:%M')}),
          'work_time_s':DateTimeInput(attrs={"type": "datetime-local", "value": timezone.datetime.now().strftime('%Y-%m-%dT%H:%M')}),
          }