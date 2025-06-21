"""
command:
insert,print,remove,append,sort,pop,reverse
"""
if __name__ == '__main__':
  ourlist = []
  N = int(input())
  for _ in range(N):  # _ bize bu for döngüsünün sadece bir say döndürdüğünü ifade eder.
      command = input(
          "Please write your list command first and then the numbers you will operate with a space between them.").split()  # burda aslında birden fazla komut alınır string artı sayısal değerler
      # split sayesinde bu string ve rakamlar arasına boşluk bırakılır ve bunlar command adlı bir listeye eklenir,indexleri 0 dan başlar pek ala
      if command[0] == "insert":#herhangi bir indexe bir eleman eklenebilir
          ourlist.insert(int(command[1]), int(command[2]))
      elif command[0] == "print":
          print(ourlist)
      elif command[0]=="remove":#listeden istenilen eleman silinir index değil,direk eleman
          try:
           ourlist.remove(int(command[1]))
          except IndexError:
              print("The list is empty")
      elif command[0]=="append":#sondan eleman eklenir
          ourlist.append(int(command[1]))
      elif command[0]=="sort":#elemanlar sıralanır
          ourlist.sort()
      elif command[0] == "pop":#kullanıcı isterse istenilen index ten elemanı siler,sadece pop yazarsa sondan eleman silinir
          try:
              if len(command) == 1:
                  ourlist.pop()
              else:
                  ourlist.pop(int(command[1]))
          except IndexError:
              print("The list is empty")

      elif command[0]=="reverse":#listeyi ters çevirir
          ourlist.reverse()
