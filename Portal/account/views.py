from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes

from django.views.generic.base import TemplateView
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationVForm, RegistrationOForm, DodatniPodaciCreationForm
from .models import User, DodatniPodaci
from ankete.models import Anketa
from django.views.generic.edit import CreateView
from forum.models import Diskusija
from oglasi.models import Oglas
from django.views import View
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.urls import reverse
from django.db.models import Q



def index_view(request):
    if request.user.is_authenticated:

        if request.user.is_staff:
            administratori = User.objects.filter(is_staff=True)
            diskusije = Diskusija.objects.all()
            oglasi = Oglas.objects.all()
            ankete = Anketa.objects.all()
            context = {
                'ankete': ankete,
                'administratori': administratori,
                'diskusije': diskusije,
                'oglasi': oglasi
            }
            return render(request, 'index.html', context)

        else:
            if request.user.first_name:

                administratori = User.objects.filter(is_staff=True)
                diskusije = Diskusija.objects.filter(
                    Q(vidljivost=1)
                    |
                    Q(vidljivost=2)
                    |
                    Q(autor=request.user)
                )
                oglasi = Oglas.objects.all()
                ankete = Anketa.objects.all()
                context = {
                    'ankete': ankete,
                    'administratori': administratori,
                    'diskusije': diskusije,
                    'oglasi': oglasi
                }

                return render(request, 'index.html', context)

            else:
                administratori = User.objects.filter(is_staff=True)
                diskusije = Diskusija.objects.filter(Q(vidljivost=1) | Q(vidljivost_za_org=1) | Q(autor=request.user))
                oglasi = Oglas.objects.all()
                ankete = Anketa.objects.all()

                context = {
                    'ankete': ankete,
                    'administratori': administratori,
                    'diskusije': diskusije,
                    'oglasi': oglasi
                }

                return render(request, 'index.html', context)

    else:
        administratori = User.objects.filter(is_staff=True)
        diskusije = Diskusija.objects.filter(vidljivost=1)
        oglasi = Oglas.objects.filter(vidljivost=1)
        context = {
            'administratori': administratori,
            'diskusije': diskusije,
            'oglasi': oglasi
        }

        return render(request, 'index.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, 'account/login.html')


class Registration_vview(CreateView):
    model = User
    form_class = RegistrationVForm
    template_name = 'register.html'

    def get_success_url(self):
        return reverse("login")

    def post(self, request, *args, **kwargs):
        result = super(Registration_vview, self).post(request, args, kwargs)

        if self.object is not None:
            self.object.is_active = False
            self.object.save()

            currentSite = get_current_site(request)
            userId = self.object.id
            coddedUserId = urlsafe_base64_encode(force_bytes(userId))

            tokenGenerator = PasswordResetTokenGenerator()

            token = tokenGenerator.make_token(self.object)

            context = {
                "user": self.object,
                "domain": currentSite.domain,
                "userId": coddedUserId,
                "token": token,
            }

            body = render_to_string("account/email.html", context)

            email = EmailMessage(
                "Активација налога - Портал за волонтирање",
                body,
                "admin@email.com",
                [self.object.email]
            )
            email.send()

        return result


class Registration_oview(CreateView):
    model = User
    form_class = RegistrationOForm
    template_name = 'org_register.html'

    def get_success_url(self):
        return reverse("login")

    def post(self, request, *args, **kwargs):
        result = super(Registration_oview, self).post(request, args, kwargs)

        if self.object is not None:
            self.object.is_active = False
            self.object.save()

            currentSite = get_current_site(request)
            userId = self.object.id
            coddedUserId = urlsafe_base64_encode(force_bytes(userId))

            tokenGenerator = PasswordResetTokenGenerator()

            token = tokenGenerator.make_token(self.object)

            context = {
                "user": self.object,
                "domain": currentSite.domain,
                "userId": coddedUserId,
                "token": token,
            }

            body = render_to_string("account/email.html", context)

            email = EmailMessage(
                "Активација налога - Портал за волонтирање",
                body,
                "admin@email.com",
                [self.object.email]
            )
            email.send()

        return result


class ActivationView(View):

    def get(self, request, userId, token):
        user = None
        try:
            id = urlsafe_base64_decode(userId).decode()
            user = User.objects.get(id=id)
        except Exception as error:
            print(error)

        if user is None:
            context = {
                "error": "Invalid id."
            }
            return render(request, "error.html", context)

        tokenGenerator = PasswordResetTokenGenerator()

        if not tokenGenerator.check_token(user, token):
            context = {
                "error": "Invalid token."
            }
            return render(request, "error.html", context)

        user.is_active = True
        user.save()

        return redirect("login")


class pregled(TemplateView):
    template_name = "account/profil.html"

    def get_context_data(self, **kwargs):
        context = super(pregled, self).get_context_data()

        dodatni_podaci = DodatniPodaci.objects.filter(volonter=self.request.user.volonter)

        if not dodatni_podaci:
            dugme = True
            interesovanja = ['Немате одабрана интересовања']
            context["interesovanja"] = interesovanja
            context['dugme'] = dugme

            return context

        volonter = DodatniPodaci.objects.get(volonter=self.request.user.volonter)

        interesovanja = volonter.interesovanja.all()

        context["interesovanja"] = interesovanja

        return context


@login_required(login_url="../../login")
def kreiranjeDodatnihPodataka(request):
    form = DodatniPodaciCreationForm()
    id = request.user.volonter
    if request.method == "POST":
        form = DodatniPodaciCreationForm(request.POST)
    if form.is_valid():
        dodatni_podatak = form.save()
        dodatni_podatak.volonter = id
        dodatni_podatak.save()
        return redirect("profil")

    context = {
        "form": form
    }

    return render(request, "account/kreirajDodatnePodatake.html", context)
