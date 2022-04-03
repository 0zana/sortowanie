#sortowanie bąbelkowe, czyli szukanie największej liczby i przesuwanie jej na koniec

L=[int(x) for x in input("wpisz liczby, które chcesz posortować (ze spacjami) ").split()]
j=0

while j<len(L):
    i=0

    while i<len(L)-1:
        if L[i]<L[i+1]:
            i=i+1
        else:
            p=L[i+1]
            L[i+1]=L[i]
            L[i]=p
            i=i+1
    j=j+1
print(L)
