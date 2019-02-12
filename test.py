from sys import argv
from back_end import *

script, file_1, file_2 = argv

def menuFileEksternal(file_1, file_2) :
    deck = open(file_1, "r")
    tampilan = open(file_2,"w")

    i = 0
    total_skor = 0

    while True:
        a = deck.readline().split()
        a = list(map(int, a))
        if a is None or len(a) == 0 or a is EOFError:
            break
        else:
            i += 1
            b = []
            a.sort(reverse=True)
            b.append(pilihOperator(a[0],a[1]))
            hasil = hitung(a[0],a[1],b[0])
            b.append(pilihOperator(hasil,a[2]))
            hasil = hitung(hasil,a[2],b[1])
            b.append(pilihOperatorTerakhir(hasil,a[3]))
            hasil = hitung(hasil,a[3],b[2])

            if (hitungHasil(a,b) == hasil) :
                tampilan.write("".join([str(a[0]), f(b[0]), str(a[1]), f(b[1]), str(a[2]), f(b[2]), str(a[3])]))
                tampilan.write("=")
                tampilan.write(str(hasil))
                tampilan.write("\n")
            else :
                if ((b[0] == 5 or b[0] == 4) and (b[1] == 3 or b[1] == 2)) :
                    tampilan.write('(',a[0], f(b[0]), a[1],')', f(b[1]), a[2], f(b[2]), a[3])
                elif ((b[1] == 5 or b[1] == 4) and (b[2] == 3 or b[2] == 2)) :
                    tampilan.write('(',a[0], f(b[0]), a[1], f(b[1]), a[2],')', f(b[2]), a[3])

            total_skor += hitungSkor(a,b,hasil)

    deck.close()
    tampilan.close()
    print("Total skor : ", total_skor)
    print("Proses berhasil dilakukan, dan hasil telah ditulis di", file_2)

menuFileEksternal(file_1, file_2);
