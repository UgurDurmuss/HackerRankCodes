def swap_case(a):
    new=[]
    for i in range(len(a)):
        if a[i].isupper():#isupper ve islower boolen bir değer döner yani true ya eşitlemen gereksiz olur
           new.append(a[i].lower())#lower harfi küçültür
        elif a[i].islower():
            new.append(a[i].upper())#upper harfi büyütür
        else :
            new.append(a[i])#bu kısım ise sayısal değerler için
    return "".join(new)#bu join yapısı önemli listeye eklediğimiz her harfi aralarında boşluk bırakarak yeni listeye ekler,parantez içine virgül bıraksaydık harflerin arasında virgül koyardı

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
