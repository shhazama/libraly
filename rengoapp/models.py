from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Comp(models.Model):
  def __str__(self) -> str:
      return self.name 
  name=models.CharField(max_length=100,verbose_name='社名')
class Planet(models.Model):
  def __str__(self) -> str:
      return self.planet
  name=models.ForeignKey(Comp,on_delete=models.CASCADE)
  planet=models.CharField(null=True,blank=True,max_length=100,verbose_name='拠点')
    
class Report(models.Model):
    def __str__(self) -> str:
        #choices リスト右側　get_***_deisplay()
        return self.write_date.strftime("%Y/%m/%d")
 
    writer=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    worker=models.CharField(max_length=100, null=True,blank=True)
    write_date=models.DateField(default=timezone.now)
    work_time_s=models.DateTimeField(null=True,blank=True)
    work_time_f=models.DateTimeField(null=True,blank=True)
    img=models.ImageField(null=True,blank=True)
    work_content=models.TextField(null=True,blank=True)
    signate=models.TextField(null=True,blank=True)
    user=models.ForeignKey(Planet, on_delete=models.CASCADE,null=True,blank=True)