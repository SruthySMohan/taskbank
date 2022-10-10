from django.urls import path,include

from . import views
app_name='bankapp'

urlpatterns = [
    path('',views.home,name='home'),
     path('login/',views.login,name='login'),
    path('logout/', views.logout, name='logout'),
    # path('signup/',views.signup,name='signup'),
    path('reg/',views.register,name='register'),
    path('reg/register',views.login,name='login'),

     path('detail/',views.detail,name='detail'),
    path('regform/',views.registerform,name='registerform'),
    path('/form',views.form,name='form'),
    path('submit/',views.submit,name='submit'),
    path('/branch',views.branch,name='branch'),
]