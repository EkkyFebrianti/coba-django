from django.contrib import admin

# Register your models here.
from .models import Barang, Jenis, member


class kolomBarang(admin.ModelAdmin):
    list_display = ['kodebrg', 'nama', 'stok', 'harga', 'link_brg', 'jenis_id']
    search_fields = ['kodebrg', 'nama']
    list_filter = ('jenis_id')
    list_per_page = 3

class kolomMember(admin.ModelAdmin):
    list_display = ['kode_member', 'nama', 'alamat', 'tahun_gabung', 'poin']
    search_fields = ['kode_member', 'nama']
    list_filter = ('poin',)
    list_per_page = 3


admin.site.register(Barang)
admin.site.register(Jenis)
admin.site.register(member, kolomMember)
