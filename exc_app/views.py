from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import User
from .forms import UserForm
from django.http.response import HttpResponseBadRequest, HttpResponse


@require_http_methods(["GET", "POST"])
def user_form(request):

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():

            User.objects.create(**form.cleaned_data)
            return HttpResponse(content="Vaše data byla uložena.")
        else:
            return HttpResponseBadRequest(
                "Některé z polí mají chybnou hodnotu či jsou nevyplněná."
            )
    else:
        form = UserForm()

    return render(request, "index.html", {"form": form})
