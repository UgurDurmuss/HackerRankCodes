if __name__ == '__main__':
    n = int(input())#burası kullanıcıdan bir girdi alır
    arr = list(map(int, input().split()))#map bir  fonksiyonu herhangi bir şeye uygulamamızı sağlayan bir nesnedir,burdaki kod bloğu kullanıcıdan input ile girdiler alıp(burdaki input herhangi
  # herhangi bir değişken almaz) split ile araya boşluk koyulmasını sağlar ve son olarak list e çevrilerek arr ile tutulur

 
    max_score = arr[0]
    for num in arr:    #listteki en büyük elemanı aldık
        if num > max_score:
            max_score = num


    filtered = [x for x in arr if x != max_score]#arr listtemizdeki büyük değerimize eşit olmayan her bir değeri filtered adli bir listeye attık,yani en büyük değeri ana listten ayrıştırmış olduk
  
  
    runner_up = filtered[0]
    for num in filtered:#tekrar aynı mantıkla sonra ki büyük elemanı bulduk yani amacımıza vardık
        if num > runner_up:
            runner_up = num

    print(runner_up)
