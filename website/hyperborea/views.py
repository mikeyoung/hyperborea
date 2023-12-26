from django.shortcuts import render

def spells(request):
    return render(request, "hyperborea/spells.html")