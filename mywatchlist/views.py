from django.shortcuts import render
from mywatchlist.models import Movies
from django.http import HttpResponse
from django.core import serializers

def bonus(request):
    jumlah = 0
    film = Movies.objects.all()
    for i in film:
        if i.watched == "Done":
            jumlah += 1
    if jumlah >= len(film) - jumlah:
        return "Selamat, kamu sudah banyak menonton!"
    else :
        return "Wah, kamu masih sedikit menonton!" 

def show_Movies(request):
    data_Movies = Movies.objects.all()
    context = {
        'list_movies' : data_Movies,
        'nama' : 'Abraham Javier Sebastian',
        'id' : '2106704364',
        'pesan' : bonus(request),
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = Movies.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Movies.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = Movies.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = Movies.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")