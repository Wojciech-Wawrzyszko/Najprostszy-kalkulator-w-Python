from django.shortcuts import render
from django.http import JsonResponse

def kalkulator(request):
    wynik = None
    wyrazenie = None
    blad = None

    if request.method == "POST":
        wyrazenie = request.POST.get("wyrazenie", "")

        if wyrazenie:
            try:
                wynik = eval(wyrazenie)
            except Exception as e:
                blad = f"Błąd: {str(e)}"

    context = {
        "wynik": wynik,
        "wyrazenie": wyrazenie,
        "blad": blad
    }

    # Żądania bez przeładowywania strony (dynamiczne obliczenia)
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse(context)

    return render(request, "kalkulator_app/index.html", context)
