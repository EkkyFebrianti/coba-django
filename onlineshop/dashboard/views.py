from django.shortcuts import render
from dashboard.forms import FormBarang
from dashboard.models import Barang, member

def Barang_View(request):
    Barangs=Barang.objects.all()
    konteks={
        'Barangs':Barangs,
    }
    return render(request,'tampil_brg.html',konteks)

def Member(request):
    Members=member.objects.all()
    konteks={
        'Members':Members,
    }
    return render(request,'member.html',konteks)

def produk(request):
    titelnya="Produk"
    konteks = {
        'titel':titelnya,
    }
    return render(request, 'produk.html',konteks)
  
# Create your views here.

def tambah_barang(request):
    form=FormBarang()
    konteks={
        'form':form,
    }
    return render(request, 'tambah_barang.html',konteks)

