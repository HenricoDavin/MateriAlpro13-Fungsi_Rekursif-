import timeit
def pangkat_rumus(x,n):
    return x**n

def pangkat_perulangan(x,n):
    hasil = 1
    for i in range(1,n+1):
        hasil = hasil*x
    return hasil

def pangkat_rekursif(x,n):
    if x == 1:
        return 1
    elif n == 1:
        return x
    elif n == 0:
        return 1
    else:
        return pangkat_rekursif(x,n-1) * x

mulai = timeit.default_timer()
hasil = pangkat_rumus(11,129)
selesai = timeit.default_timer()
waktu = selesai - mulai
print(f'Hasil: {hasil}')
print(f'Waktu: {waktu}')

mulai = timeit.default_timer()
hasil = pangkat_perulangan(11,129)
selesai = timeit.default_timer()
waktu = selesai - mulai
print(f'Hasil: {hasil}')
print(f'Waktu: {waktu}')

mulai = timeit.default_timer()
hasil = pangkat_rekursif(11,129)
selesai = timeit.default_timer()
waktu = selesai - mulai
print(f'Hasil: {hasil}')
print(f'Waktu: {waktu}')