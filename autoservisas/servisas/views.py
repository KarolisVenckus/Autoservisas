from django.shortcuts import render, redirect
from .models import Paslauga, PaslaugosKaina, AutomobilioModelis, Automobilis, TaisymoUzsakymas

def paslaugu_ivestis(request):
    if request.method == 'POST':
        # Handle the form submission
        pavadinimas = request.POST['pavadinimas']
        kaina = request.POST['kaina']
        
        # Save the data to the database
        paslauga = Paslauga.objects.create(pavadinimas=pavadinimas)
        PaslaugosKaina.objects.create(paslauga=paslauga, kaina=kaina)
        
        return redirect('paslaugos_sarasas')  # Redirect to the service list page
    else:
        return render(request, 'servisas/paslaugos.html')
