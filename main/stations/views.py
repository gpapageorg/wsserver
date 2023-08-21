from django.shortcuts import render, redirect

def fortosi(request):
    if request.user.is_authenticated:

        return render(request, "fortosi.html",{})
    else:
        return redirect('login')
    
def patras(request):
    if request.user.is_authenticated:

        return render(request, "patras.html",{})
    else:
        return redirect('login')
    
def kosmira(request):
    if request.user.is_authenticated:

        return render(request, "kosmira.html",{})
    else:
        return redirect('login')