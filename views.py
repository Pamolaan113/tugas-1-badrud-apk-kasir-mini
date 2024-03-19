from django.shortcuts import render, redirect
from .models import Menu, Transaksi

def index(request):
    menu = Menu.objects.all()
    context = {'menu': menu}
    return render(request, 'index.html', context)

def tambah_transaksi(request):
    if request.method == 'POST':
        menu_id = request.POST['menu']
        jumlah = request.POST['jumlah']
        menu = Menu.objects.get(pk=menu_id)
        total_harga = menu.harga * int(jumlah)
        transaksi = Transaksi(menu=menu, jumlah=jumlah, total_harga=total_harga)
        transaksi.save()
        return redirect('index')

def laporan(request):
    transaksi = Transaksi.objects.all()
    context = {'transaksi': transaksi}
    return render(request, 'laporan.html', context)