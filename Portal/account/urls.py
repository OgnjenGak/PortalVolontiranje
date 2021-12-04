from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from django.contrib.auth import views as av


urlpatterns = [
    path('', views.index_view, name='index'),
    path("logout/", views.logoutUser, name='logout'),
    path("login/", LoginView.as_view(template_name="account/login.html"), name="login"),
    path("register/", views.Registration_vview.as_view(template_name="account/register.html"), name="register"),
    path("org_register/", views.Registration_oview.as_view(template_name="account/org_register.html"),
         name="org_register"),

    path("activate/<userId>/<token>", views.ActivationView.as_view(), name="activation"),

    path('password_reset/',
         av.PasswordResetView.as_view(
             template_name="account/password_reset.html",
             html_email_template_name='account/password_reset_html_email.html'),
         name="reset_password"),

    path("reset_password_sent/",
         av.PasswordResetView.as_view(template_name="account/password_reset_sent.html"),
         name="password_reset_done"),

    path("reset/<uidb64>/<token>/",
         av.PasswordResetConfirmView.as_view(template_name="account/password_reset_form.html"),
         name="password_reset_confirm"),

    path("reset_password_complete/",
         av.PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"),
         name="password_reset_complete"),

    path('dodatni_podaci/', views.kreiranjeDodatnihPodataka, name='kreiranjeDodatnihPodataka'),
    path('profil/', views.pregled.as_view(), name="profil"),
]
