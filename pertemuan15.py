
#pertemuan 15

1.
'''
1: Membuat dan Mengakses
-. Buat sebuah dictionary bernama biodata untuk merepresentasikan dirimu. Isinya harus memiliki
key: "nama", "umur", "hobi" (hobi bisa berupa list dari beberapa string), dan
"sudah_menikah" (berisi boolean).
/. Cetak seluruh dictionary.
0. Cetak hanya value dari key "nama".
1. Cetak hobi pertamamu dari list hobi
'''
biodata = {
    "nama" : "Ahmad Faiz",
    "umur" : 17,
    "hobi" : ["olahraga","membaca buku","berpetualangan"],
    "sudah menikah" : False,
}
print(biodata)
print(biodata["nama"])
print(biodata["hobi"][0])

2.
'''
: Modifikasi Dictionary
-. Gunakan dictionary biodata dari Latihan 1.
/. Tambahkan pasangan key-value baru: "kota": "Nama Kotamu".
0. Ubah value dari key "umur" menjadi umurmu tahun depan.
1. Cetak dictionary yang sudah diperbarui.
'''
biodata = {
    "nama" : "Ahmad Faiz",
    "umur" : 17,
    "hobi" : ["olahraga","membaca buku","berpetualangan"],
    "sudah menikah" : False,
    "kota" : "bekasi",
}
biodata["umur"] += 1
print(biodata)

3.
'''
Penggunaan .get()
-. Masih dengan dictionary biodata.
/. Coba akses key "pekerjaan" menggunakan bracket notation []. Apa yang terjadi? (Beri komentar
pada baris ini agar tidak error).
0. Sekarang, akses key "pekerjaan" menggunakan metode .get(). Cetak hasilnya.
1. Akses lagi key "pekerjaan" menggunakan .get(), tapi kali ini berikan nilai default "Pelajar".
Cetak hasilnya.
'''
biodata = {
    "nama" : "Ahmad Faiz",
    "umur" : 17,
    "hobi" : ["olahraga","membaca buku","berpetualangan"],
    "sudah menikah" : False,
    "kota" : "bekasi",
}
print(biodata.get("pekerjaan")) 
print(biodata.get("pekerjaan", "Pelajar"))

4.
'''
Histogram Kata
Buat program yang:
-. Meminta pengguna memasukkan sebuah kalimat.
/. Membuat histogram (dalam bentuk dictionary) yang menghitung frekuensi setiap kata (bukan
huruf) dalam kalimat tersebut.
0. Cetak dictionary histogram tersebut.
Petunjuk: Gunakan metode .split() untuk mengubah kalimat menjadi list kata-kata terlebih
dahulu. Abaikan huruf besar/kecil dengan mengubah seluruh kalimat menjadi lowercase di awal.
'''
kalimat = input("Masukkan kalimat: ")
kata_kata = kalimat.lower().split()
histogram = {}
for kata in kata_kata:
    if kata in histogram:
        histogram[kata] += 1
    else:
        histogram[kata] = 1
print("Histogram kata:", histogram)




