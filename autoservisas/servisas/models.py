from django.db import models

class Paslauga(models.Model):
    pavadinimas = models.CharField(max_length=100)

class PaslaugosKaina(models.Model):
    paslauga = models.ForeignKey(Paslauga, on_delete=models.CASCADE)
    kaina = models.DecimalField(max_digits=8, decimal_places=2)

class AutomobilioModelis(models.Model):
    metai = models.IntegerField()
    marke = models.CharField(max_length=100)
    modelis = models.CharField(max_length=100)
    variklis = models.CharField(max_length=100)

class Automobilis(models.Model):
    automobilio_id = models.CharField(max_length=100)
    klientas = models.CharField(max_length=100)
    valstybinis_numeris = models.CharField(max_length=100)
    vin_kodas = models.CharField(max_length=100)

class TaisymoUzsakymas(models.Model):
    automobilis = models.ForeignKey(Automobilis, on_delete=models.CASCADE)
    bendra_suma = models.DecimalField(max_digits=8, decimal_places=2)
    # Laikykite paslaugas, kiekius ir kainas JSON formatu (pavyzdžiui, {'paslauga': 'Alyvos keitimas', 'kiekis': 1, 'kaina': 50.00})
    atliktos_paslaugos = models.JSONField()