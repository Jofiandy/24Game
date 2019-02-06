def hitung(num1,num2,op):
    if (op == 5) :
        return (num1 + num2)
    elif (op == 4) :
        return (num1 - num2)
    elif (op == 3) :
        return (num1 * num2)
    elif (op == 2) :
        if (num2 != 0):
            return float(num1)/float(num2)

def pilihOperator(num1,num2) :
    hasil = []
    hasil.append(hitung(num1,num2,2))
    hasil.append(hitung(num1,num2,3))
    hasil.append(hitung(num1,num2,4))
    hasil.append(hitung(num1,num2,5))
    for i in [3,2,1,0] :
        if (selisih(hasil[i],24) == 0) :
            return (i + 2)
            break
        hasil[i] = (i + 2) - selisih(hasil[i],24)

    return (hasil.index(max(hasil)) + 2)

def hitungHasil(a,b) :
    hasil_1 = 0
    hasil_2 = 0
    if (b[0] <= b[1] and b[1] <= b[2]):
        hasil_1 += hitung(a[0],a[1],b[0])
        hasil_1 = hitung(hasil_1,a[2],b[1])
        hasil_1 = hitung(hasil_1,a[3],b[2])
    elif (b[0] <= b[2] and b[2] <= b[1]) :
        hasil_1 += hitung(a[0],a[1],b[0])
        hasil_2 += hitung(a[2],a[3],b[2])
        hasil_1 = hitung(hasil_1,hasil_2,b[1])
    elif (b[1] <= b[0] and b[0] <= b[2]) :
        hasil_1 += hitung(a[1],a[2],b[1])
        hasil_1 = hitung(a[0],hasil_1,b[0])
        hasil_1 = hitung(hasil_1,a[3],b[2])
    elif (b[1] <= b[2] and b[2] <= b[0]) :
        hasil_1 += hitung(a[1],a[2],b[1])
        hasil_1 = hitung(hasil_1,a[3],b[2])
        hasil_1 = hitung(a[0],hasil_1,b[0])
    elif (b[2] <= b[0] and b[0] <= b[1]) :
        hasil_1 += hitung(a[2],a[3],b[2])
        hasil_2 += hitung(a[0],a[1],b[0])
        hasil_1 = hitung(hasil_2,hasil_1,b[1])
    else :
        hasil_1 += hitung(a[2],a[3],b[2])
        hasil_1 = hitung(a[1],hasil_1,b[1])
        hasil_1 = hitung(a[0],hasil_1,b[0])
    return hasil_1

def selisih(x,y) :
    if (x >= y) :
        return (x-y)
    else :
        return (y - x)

def f(x):
    if (x == 5) :
        return '+'
    elif (x == 4) :
        return '-'
    elif (x == 3) :
        return '*'
    else :
        return '/'

def hitungSkor(a, b, hasil) :
    if (hitungHasil(a,b) == hasil) :
        return (b[0] + b[1] + b[2] - selisih(24,hitungHasil(a,b)))
    else :
        return (b[0] + b[1] + b[2] - selisih(24,hasil) - 1)

def tampilEkspresi(a,b, hasil) :
    if (hitungHasil(a,b) == hasil) :
        print(a[0], f(b[0]), a[1], f(b[1]), a[2], f(b[2]), a[3])
    else :
        if ((b[0] == 5 or b[0] == 4) and (b[1] == 3 or b[1] == 2)) :
            print('(',a[0], f(b[0]), a[1],')', f(b[1]), a[2], f(b[2]), a[3])
        elif ((b[1] == 5 or b[1] == 4) and (b[2] == 3 or b[2] == 2)) :
            print('(',a[0], f(b[0]), a[1], f(b[1]), a[2],')', f(b[2]), a[3])

def menuGame() :
    a = []
    b = []
    n = int(input("Bilangan 1 > "))
    a.append(n)
    n = int(input("Bilangan 2 > "))
    a.append(n)
    n = int(input("Bilangan 3 > "))
    a.append(n)
    n = int(input("Bilangan 4 > "))
    a.append(n)
    a.sort(reverse=True)
    b.append(pilihOperator(a[0],a[1]))
    hasil = hitung(a[0],a[1],b[0])
    b.append(pilihOperator(hasil,a[2]))
    hasil = hitung(hasil,a[2],b[1])
    b.append(pilihOperator(hasil,a[3]))
    hasil = hitung(hasil,a[3],b[2])

    tampilEkspresi(a,b,hasil)
    print("Hasil perhitungan = ", hasil)
    print("Skor = ", hitungSkor(a,b,hasil))

def menuFileEksternal() :
    deck = open("input.txt", "r")
    tampilan = open("output.txt","w")

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
            b.append(pilihOperator(hasil,a[3]))
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

print("Selamat datang di permainan 24")
print("1. User")
print("2. File")
pilihan = int(input("> "))
if (pilihan == 1):
    menuGame()
else :
    menuFileEksternal();