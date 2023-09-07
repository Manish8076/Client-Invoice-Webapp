"""
URL configuration for netcore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from netcores import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.signup , name='signUp'),
    path('', views.login_view , name='login'),
    path('dashboard/', views.dashboard , name='dashboard'),
    path('logout/', views.logout_view , name='logout'),
    path('add_invoice/', views.add_invoice , name='addInvoice'),
    path('add_invoice2/', views.add_invoice2 , name='addInvoice2'),
    path('service_provider/', views.serviceProvider , name='service_provider'),
    path('update_company/<int:id>', views.update_company , name='update_company'),
    path('delete_company/<int:id>/', views.delete_company, name='delete_company'),
    path('all_list/', views.all_list , name='all_list'),
    path('update_client/<int:id>', views.update_client , name='update_client'),
    path('delete_client/<int:id>/', views.delete_client, name='delete_client'),
    path('review/<int:pk>/', views.review, name='review'),
    path('update_services/<int:id>', views.update_services , name='update_services'),
    path('delete_services/<int:id>/', views.delete_services, name='delete_services'),
    path('invoice_report/' ,views.invoice_report, name='invoice_report'),
    path('gst_report/<int:pk>' ,views.gst_report, name='gst_report'),
   

    
    
]



