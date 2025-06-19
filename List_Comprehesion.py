if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

x=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)#döngüler iç içe sıralı çalışır; önce i sabitken j tüm değerleri alır, her j için k tüm değerleri alır
if i+j+k!=n]#i,j,k üzerinden birkaç tane for açtık taska göre değerlerimiz sıfırdan
#başlıyor zaten bunun için range kullanık ve girilen x y z değerlerine göre i,j,k leri
#list comprehension ile belirledik,i j k değerlerinin toplamı sınır olan n e eşit olan list'leri çıkardık

print(x)#herhangi bir değere eşitleyip yazdık list comprehesionu
