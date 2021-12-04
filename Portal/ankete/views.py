from django.shortcuts import render
from .forms import AnketeCreateForm
from django.shortcuts import redirect
from .forms import Glasovi
from .models import Anketa, Stavka
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="../../login")
def kreiranjeAnkete(request):

    form = AnketeCreateForm()
    if request.method == "POST":
        form = AnketeCreateForm(request.POST)
    if form.is_valid():
        anketa = form.save()
        anketa.autor_ankete = request.user
        anketa.save()
        return redirect("index")

    context = {
        "form": form
    }

    return render(request, "ankete/kreiranje_ankete.html", context)


def anketa(request):
    if request.method == "GET":
        id = request.GET.get("id")
        anketa = Anketa.objects.get(id=id)
        odgovori = Stavka.objects.filter(pitanje=anketa)
        odg_vol = Stavka.objects.filter(pitanje=anketa, ispitanik=request.user)
        form = Glasovi()
        print(odgovori)
        context = {
            'odg_vol': odg_vol,
            'odgovori': odgovori,
            'anketa': anketa,
            'form': form,
        }
        print("GET", context)
        return render(request, 'ankete/anketa.html', context)

    elif request.method == "POST":
        id = request.POST.get('id')
        odgovor = Glasovi(request.POST)
        anketa = Anketa.objects.get(id=id)
        odgovori = Stavka.objects.filter(pitanje=anketa)

        if odgovor.is_valid():
            odgovor = odgovor.save(commit=False)
            odgovor.pitanje = anketa
            odgovor.ispitanik = request.user
            odgovor.save()

        context = {
            'odgovori': odgovori,
            'anketa': anketa,
        }

        print("POST", context)
        return render(request, 'ankete/anketa.html', context)
