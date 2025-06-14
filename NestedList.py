if __name__ == '__main__':
    our_list=[]
    new_list=[]
    stu_num=0
    for _ in range(int(input("how many time rolling our list "))):#kullanıcıdan bir girdi alır,integera çevirir,for_in range mantığı döngüyü kullanıcının girdiği sayı kadar çalıştırır
        name = input("please enter the name ")
        score = float(input("what is his/her score "))
        stu_num=stu_num+1
        our_list.append([name,score])#append her zaman tek bir argüman alır



    print(f"our_list={our_list}")

    x=1
    max_index=0
    big_score=our_list[0][x]
    for a in range(1,stu_num):
        if our_list[a][x]>big_score:
            big_score=our_list[a][x]
            max_index=a
    print(f"big_score is ={big_score}")

    #new_list=our_list[:max_index]+our_list[max_index+1:]#pythonda slicing mantığı
    #[start:step:stop:] ,[start:stop]  stopta her zaman bir eksiği olan indexe kadar gider
    #başlangıç ve bitiş indexlerinden başlayarak parçalayıp yeni listeye ekledik

    new_list = [item for item in our_list if item[1] != big_score]

    print(f"new list = {new_list}")


    new_big = new_list[0][x]
    for a in range(1, len(new_list)):#out of range olmasın diye son çıkarılan elemanlardan kalan listenin uzunluğunu len iel aldım
        if new_list[a][x] > new_big:
            new_big = new_list[a][x]
    names=[]
    for name,score in new_list:
        if score==new_big:
            names.append(name)
    names_sorted=sorted(names)#isimleri alfabetik sıraya göre dizer

    print(f"en büyük skora sahip kişiler={names_sorted}")
