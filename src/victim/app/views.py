from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login_view(request):
    if request.method == "POST":
        user = authenticate(username=request.POST["u"], password=request.POST["p"])
        if user:
            login(request, user)
            return HttpResponse("Logado com sucesso")
    return render(request, "login.html")

# XSS refletido
def vulnerable_page(request):
    msg = request.GET.get("msg", "")
    return HttpResponse(f"<h1>Mensagem: {msg}</h1>")