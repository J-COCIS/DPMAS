from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
path('', views.home, name='home'),
path('category/', views.category, name='category'),
path('reg_user_patient/', views.registerUserPatient, name='reg_user_patient'),
path('reg_user_doctor/', views.registerUserDoctor, name='reg_user_doctor'),
path('login/', views.loginView, name='login'),
path('patient/', views.patient_home, name='patient'),
path('otp_verification1/',views.otp_verification1,name="otp_verification1"),
path('otp_verification2/',views.otp_verification2,name="otp_verification2"),
path('create_profile/', views.create_profile, name='create_profile'),
path('diagnosis/', views.diagnosis, name='diagnosis'),
path('diagnosis/predict', views.MakePredict, name='predict'),
path('result/', views.patient_result, name='result'),
path('result/ment', views.MakeMent, name='ment'),
path('ment/', views.patient_ment, name='ment_list'),
path('logout/', views.logoutView, name='logout'),
path('doctor/', views.doctor_home, name='doctor'),
path('commend/', views.doctor_commend, name='commend'),
path('commend/predict', views.MakeMend, name='mend'),
path('meet/', views.doctor_ment, name='meet_list'),
path('meet/save/', views.SaveMent, name='savement'),
path('doctors/', views.doctor_list, name='dr_list'),
path('about/', views.about, name='about'),
path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]