from django.contrib import admin
from django.urls import path
from bank import views
app_name = "bank" 
urlpatterns = [
    path("y/",views.yod,name="y"),
    path("b/",views.cus,name="b"),
    path("m/",views.dat,name="m"),
    path("c/",views.cere,name="c"),
    path("de/",views.debi,name="de"),
    path("home/",views.homepage,name='home'),
    path("actionpage/<int:Account_no>/<str:Customer_NAME>/<str:Balance>/",views.actionpage,name='actionpage'),
    path("credit/<int:Account_no>/",views.credit,name='credit'),
    path("credit/",views.credit,name='credit'),
    path("debit/<int:Account_no>",views.Debit,name='debit'),
    path("debit/",views.Debit,name='debit'),
    path("bal/",views.balance_enquiry,name='bal'),
    path("success/<int:Account_no>/<str:Customer_NAME>/<str:Balance>/",views.success_page,name='success_page'),
    path("s/",views.nuser,name='s'),
    path("u/",views.newuser,name='u'),
    path("uc/",views.user_created,name='uc'),
    path("cu/",views.c_user,name='cu'),
] 