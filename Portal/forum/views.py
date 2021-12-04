from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import DiskusijaCreateForm, KomentarCreateForm
from .models import Diskusija
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="../../login")
def kreiranjeDiskusije(request):
    create_form = DiskusijaCreateForm()
    form = create_form

    if request.method == "POST":
        form = DiskusijaCreateForm(request.POST)
        if form.is_valid():
            diskusija = form.save()
            diskusija.autor = request.user
            diskusija.save()
            return redirect("index")

    context = {
        "form": form
    }

    return render(request, "forum/kreirajDiskusiju.html", context)


@login_required(login_url="../../login")
def dodajKomentar(request):
    id = request.POST.get("id")
    form = KomentarCreateForm(request.POST)

    diskusija = Diskusija.objects.get(id=id)

    if form.is_valid():
        komentar = form.save(commit=False)
        komentar.diskusija = diskusija
        komentar.autor = request.user
        komentar.save()

        context = {
            "komentari": diskusija.komentar_set.all()
        }

        result = render_to_string("forum/dodajKomentar.html", context, request)

        return HttpResponse(result)

    else:
        data = {}
        for field in form:
            key = field.auto_id + '_errors'
            data[key] = str(field.errors)

        return JsonResponse(data, status=400)


def diskusija(request):
    if request.method == "GET":
        id = request.GET.get("id")
        diskusija = Diskusija.objects.get(id=id)

        form = KomentarCreateForm()

        context = {
            'diskusija': diskusija,
            'form': form,
        }
        print("GET", context)
        return render(request, 'forum/diskusija.html', context)

    elif request.method == "POST":
        id = request.POST.get("id")
        form = KomentarCreateForm(request.POST)

        diskusija = Diskusija.objects.get(id=id)

        if form.is_valid():
            komentar = form.save(commit=False)
            komentar.diskusija = diskusija
            komentar.autor = request.user
            komentar.save()
            form = KomentarCreateForm()

        context = {
            "diskusija": diskusija,
            "form": form
        }
        print("POST", context)
        return render(request, "forum/diskusija.html", context)
