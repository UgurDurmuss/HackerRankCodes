if __name__ == '__main__':
    n = int(input("how many people do you add list "))
    student_marks = {}#bu boş bir dict,içinde anahtar değer eşleşmeleri vardır
    for _ in range(n):
        name, *line = input().split()#burda ilkin bir isim girilir,*line kısmı dict imize ait key olur
        #line kısmı ise anahtar(lar) olur.mesela name=ali line=(23 24 25) olur
        scores = list(map(float, line))#map sayesinde line'deki tüm değerleri float yaparı ve listeleriz
        student_marks[name] = scores#ve işte anahtar değer eşleşmesi,isim artı skorlar
    query_name = input("which person do you want its notes average")#hedef kişi
    #print(student_marks)
    average=0
    for value in student_marks[query_name]:
        average=sum(student_marks[query_name])/len(student_marks[query_name])#değerleri value cinsinden aldığımız için,sum sayesinde istenilen değerin tüm value değerlerini aldık,len sayesinde bunların saysısını
    print("{:.2f}".format(average))#virgülden sonra iki basamağıda alır
