from django.urls import path
from . import views

urlpatterns = [
    path('home/report/sign',views.SignView.as_view(),name='reportsign'),
    path('home/',views.HomeView.as_view(),name='home'),
    path('customer/create/', views. CreateCustomerView.as_view(),name='create-customer'),
    path('home/<int:pk>/menu/',views.FarmMenuView.as_view(),name='farm-menu'),
    path('home/menu/reports/<str:user>/',views.reportlist_view,name='report-list'),
    path('home/menu/newreports/create/', views. CreateReportView.as_view(),name='create-report'),
    #path('home/menu/report/number/<int:pk>/',views.report_detail_view,name='report-detail'),
    path('home/menu/report/number/<int:pk>/',views.DetailPlaceView.as_view(),name='report-detail'),
    path('report/<int:pk>/delete/', views.DeleteReportView.as_view(),name='delete-report'),
    path('report/<int:pk>/update/', views.UpdateReportView.as_view(),name='update-report'),
 ]