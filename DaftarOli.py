"""
@author: Fery A
"""
#Daftar Harga oli motor:
#Duration SW20 1L       @53.0000
#Castrol Magnatec 1L    @50.0000
#Federal Supreme XX 1L  @54.0000
#Yamalube 1L            @45.0000
#Shell 1L               @46.0000

#jika menggunakan list Kode dibawah ini, maka metode yang digunakan
#adalah mendeteksi indeks value yang terpilih pada list kode.
#caranya: melakukan pencarian pada list kode menggunakan 
#nilai kode yang diinputkan
#salah satu metode : gunakan while
  
jwb = "y"

while jwb=="y" or jwb=="Y":
    print("=========================================")
    print(" DAFTAR HARGA OLI ")
    print("=========================================")
    print("a = Duration SW20 1L")
    print("b = Castrol Magnatec 1L")
    print("c = Federal Supreme XX 1L")
    print("d = Yamalube 1L")
    print("e = Shell 1L")
    print("=========================================")
    print(" ")

    #algoritma:
    # baca berulang2 index dalam list kode, jika value sama dengan 
    # value pilihan, ambil index nya
    kode    = ['a','b','c','d','e']
    oli     = ['Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L',' Shell 1L']
    harga   = ['53000','50000','54000','45000','46000']

    #identifikasi Indeks list berdasarkan pilihan
    pilihan = input(">> Masukkan Kode Oli = ")
    if pilihan=="a" or pilihan=="A" :
        idx = 0
    elif pilihan=="b" or pilihan=="B" :
        idx = 1
    elif pilihan=="c" or pilihan=="C" :
        idx = 2
    elif pilihan=="d" or pilihan=="D" :
        idx = 3
    elif pilihan=="e" or pilihan=="E" :
        idx = 4
    else:
        idx =0
    print(">>> Pilihan Oli      = " + oli[idx])
    print(">>> Harga            = Rp. " + str(harga[idx]))

    #tahap hitung biaya
    n = input("Masukkan Banyaknya oli yang akan dibeli = ")
    x = int(n)
    TotalAwalA = x * int(harga[idx])

    #Tahap menghitung diskon
    #mendapatkan diskon ketika pembelian bernilai < 200.000 = 5%
    TotalMinimalSebelumppn = 200000 
    if TotalAwalA < TotalMinimalSebelumppn : 
        TotalAwalB = TotalAwalA - TotalAwalA*5/100
    else:
        TotalAwalB = TotalAwalA

    #TotalBiaya Dengan PPN 1%
    TotalAkhir = TotalAwalB + TotalAwalB*1/100

    #tampilkan Total Biaya
    print(">>>> Total Akhir     = Rp. " + str(TotalAkhir))
    print(" ")
    print("==============================================")
    jwb = input(">> Mau mengulangi ? y/t = ")
    if jwb=="t" or jwb=="T":
        break