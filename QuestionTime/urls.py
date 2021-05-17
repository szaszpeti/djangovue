"""QuestionTime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from core.views import IndexTemplateView

#http://django-registration.readthedocs.io
from django_registration.backends.one_step.views import RegistrationView
from users.forms import CustomUserForm

urlpatterns = [
    path('admin/', admin.site.urls),
    #path to this custom version of the registration view provieded by django registration
    #that we used to create new accounts via url browser
    path("accounts/register/", RegistrationView.as_view(
    	form_class=CustomUserForm,
    	success_url="/"), name="django_registration_register"),

    #then we have other urls used by the django reg package
    path("accounts/", include("django_registration.backends.one_step.urls")),

    #the log in url provided by django to log in unser via a browser
    path("accounts/", include("django.contrib.auth.urls")),


    #login url for the browser API 
    path("api/", include("users.api.urls")),

    path("api/", include("questions.api.urls")),

    path("api-auth/", include("rest_framework.urls")),

    #the login endpoints to use via rest 
    path("api/rest-auth/", include("rest_auth.urls")),
    #registration endpoints
    path("api/rest-auth/registration/", include("rest_auth.registration.urls")),

    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")
]
